from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from src.services.queries_service import QueriesService
from src.services.memory_service import MemoryService
from src.middleware.data_token import TokenUsers


class ChatService:

    def __init__(self):
        self.memory = MemoryService()
        self.data_token = TokenUsers()
        self.queries_service = QueriesService()
        self.model = OllamaLLM(
            model="gemma3:4b",
            temperature=0.3,  # Reduce la temperatura 
            num_ctx=1024,     # Aumenta el contexto
            top_k=20,         
            top_p=0.85,
            max_tokens=300
        )
        

        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", """Eres un experto en agricultura llamado AgroBot. Tu función es asistir en monitoreo de cultivos 
            usando datos de sensores y configuraciones del usuario. Sigue estrictamente estas reglas:
            
            1. Usar SIEMPRE los datos proporcionados en este orden:
               - Ubicación: {address}
               - Lecturas : {reads}
               - Alertas activas: {alerts}
               - Historial de conversacion: {chat_history}
               
            2. Respuestas deben ser en español claro y estructurado con:
               - Análisis breve de datos
               - Recomendaciones específicas
               - Consideraciones adicionales
               
            3. Si faltan datos importantes, solicitar amablemente la información.
            
            4. Mantener respuestas técnicas pero accesibles, usando máximo 3 párrafos.
            
            """),
            
            ("human", "{question}")
        ])

    def chat(self, token, message):
        user_id = self.data_token.extract_user_info(token)[0]
        chat_history = self.memory.get_chat_history(user_id)

        reads = self.queries_service.get_reads(token)
        alerts = self.queries_service.get_alerts(token)
        address = self.queries_service.get_adress() 

        input_data = {
            "chat_history": chat_history, 
            "question": message,
            "reads": reads,
            "alerts": alerts,
            "address": address
        }

        chain = self.prompt_template | self.model 
        response = chain.invoke(input_data)

        self.memory.save_message(user_id, message, response)

        return response