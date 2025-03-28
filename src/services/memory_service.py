from redis import Redis
from langchain_community.chat_message_histories import RedisChatMessageHistory
from langchain.schema import AIMessage, HumanMessage
from src.core.config import Settings

class MemoryService:
    def __init__(self):
        self.redis_url = f"redis://{Settings.REDIS_HOST}:{Settings.REDIS_PORT}"
        self.memory = {}

    def get_user_memory(self, user_id: str):
        """Obtenemos la memoria del usuario en Redis."""
        user_id = str(user_id)

        if user_id not in self.memory:
            self.memory[user_id] = RedisChatMessageHistory(
                session_id=user_id,
                url=self.redis_url
            )
        return self.memory[user_id]

    def save_message(self, user_id: str, user_message: str, response_ia: str):
        """Guarda los mensajes en Redis."""
        memory = self.get_user_memory(user_id)
        memory.add_message(HumanMessage(content=user_message))
        memory.add_message(AIMessage(content=response_ia))

    def get_chat_history(self, user_id: str):
        """Obtiene el historial del chat del usuario."""
        memory = self.get_user_memory(user_id)
        return memory.messages if memory.messages else []