# api/chatbot_api.py

from fastapi import HTTPException
from models.src.heuristic_bot import HeuristicBot

async def conversation(user_input):
    EXIT_COMMANDS = ['none', '', 'thank you', 'bye', 'exit']
    try:
        bot = HeuristicBot()
        bot.load_model()
        
        user_input = user_input.strip().lower()
        
        if user_input in EXIT_COMMANDS:
            return {"answer": "Feel happy to help you..."}
        
        answer = bot.chatbot(user_input=user_input)
        if not answer:
            answer = "Sorry, I didn't understand that."
        return {"answer": answer}
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
