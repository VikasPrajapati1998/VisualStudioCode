# main/routes/api_routes.py

from fastapi import APIRouter
from api.chatbot_api import conversation

router = APIRouter()

@router.get("/chatbot")
async def chat(question: str):
    response = await conversation(question)  # Call the conversation function
    return response
