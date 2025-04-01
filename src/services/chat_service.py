from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
from src.services.queries_service import QueriesService
from src.services.memory_service import MemoryService
from src.middleware.data_token import TokenUsers

load_dotenv()

class ChatService:

    def __init__(self):
        #self.memory = MemoryService()
        self.data_token = TokenUsers()
        self.queries_service = QueriesService()

        self.model = ChatDeepSeek(
            model_name="deepseek-chat",
            temperature=0, 
            max_tokens=None,
            timeout=None,
            max_retries=2,
            api_key=os.getenv("llm")
        )

        self.prompt_template =ChatPromptTemplate.from_messages([
            ("system", """Eres un chatbot experto en monitoreo de cultivos y en dar recomendaciones. 
            Usa la información previa y la ubicación del usuario ({address}), así como las lecturas ({reads}) 
            y alertas configuradas ({alerts}) para responder correctamente. 
            Si el usuario ya mencionó su cultivo, no preguntes de nuevo. Sé amigable y responde con empatía.
            """),
            ("human","**Pregunta:** {question}")
        ])

    def chat(self, token, message):
        try:
            
            user_id = self.data_token.extract_user_info(token)[0]
            #chat_history = self.memory.get_chat_history(user_id)
    
            reads = self.queries_service.get_reads(token)
            alerts = self.queries_service.get_alerts(token)
            address = self.queries_service.get_adress()
    
            input_data = {
                #"chat_history": chat_history,
                "question": message,
                "reads": reads,
                "alerts": alerts,
                "address": address
            }
            prompt = self.prompt_template.format_prompt(**input_data)
            response = self.model.invoke(prompt)
    
            if isinstance(response, dict) and "content" in response:
                response_text = response["content"]
            elif hasattr(response, "content"):
                response_text = response.content
            else:
                response_text = "Lo siento, no pude procesar tu solicitud correctamente."
    
            #self.memory.save_message(user_id, message, response_text)
    
            return response_text
    
        except Exception as e:
            return f"Lo siento, ocurrió un error: {str(e)}"