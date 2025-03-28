import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from dotenv import load_dotenv
from src.services.chat_service import ChatService

load_dotenv()

chat_service = ChatService()

test_token = os.getenv("TEST_TOKEN")

print("IA-> Bienvenido al chatbot de monitoreo de cultivos.")
print("Escribe 'salir' para terminar la conversación.\n")

while True:
    user_message = input("Tú: ")
    
    if user_message.lower() == "salir":
        print("¡Hasta luego!")
        break

    try:
        
        response = chat_service.chat(test_token, user_message)
        print(f"IA-> Chatbot: {response}\n")
    except Exception as e:
        print(f"Error: {e}")
        break