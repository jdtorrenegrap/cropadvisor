# filepath: /home/jsust/Desktop/cropadvisor/src/models/chat_message.py
from pydantic import BaseModel

class ChatMessage(BaseModel):
    message: str