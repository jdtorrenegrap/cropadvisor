from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from src.services.memory_service import MemoryService
import json

class ChatService:

    def __init__(self):
        self.memory = MemoryService()
        self.ollama = OllamaLLM(model="gemma3:4b")
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", """Eres un chatbot experto en monitoreo de cultivos y en dar recomendaciones. 
            Usa la información previa y la ubicación del usuario ({address}), así como las lecturas ({reads}) 
            y alertas configuradas ({alerts}) para responder correctamente. 
            Si el usuario ya mencionó su cultivo, no preguntes de nuevo. Sé amigable y responde con empatía.
            """),
            ("human", "**Historial:** {chat_history}\n\n **Pregunta:** {question}")
        ])

    def chat(self, token, username, user_id, message):

        chat_history = self.memory.get_chat_history(user_id)

        reads = ""
        alerts = ""
        address = ""

        input_data = {
            "chat_history": chat_history,
            "question": message,
            "reads": reads,
            "alerts": alerts,
            "address": address
            
        }

        prompt = self.prompt_template.format(**input_data)
        response = self.model.invoke(prompt)

        return response
    