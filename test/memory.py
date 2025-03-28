import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from src.services.memory_service import MemoryService

memory_service = MemoryService()
user_id = 3

try:
    chat_history = memory_service.get_chat_history(user_id)
    print("Historial del chat:")
    for message in chat_history:
        print(f"- {message.type}: {message.content}")

except Exception as e:
    print(f"Error durante la prueba de conexión a Redis: {e}")