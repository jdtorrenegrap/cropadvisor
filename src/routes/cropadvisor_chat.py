from fastapi import Depends, APIRouter, HTTPException
from src.services.chat_service import ChatService
from src.models.chat_message import ChatMessage
from src.middleware.data_token import TokenUsers
import httpx

router = APIRouter()
chat = ChatService()

@router.post("/webhook")
async def webhook(message: ChatMessage):
    try:
        result = chat.process_webhook_message(message)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en webhook: {str(e)}")

@router.post("/cropadvisor/chat")
async def chat_message(message: ChatMessage, token: str = Depends(TokenUsers.validate_token)):
    try:
        response = chat.chat(token, message.message)
        return {"message": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))