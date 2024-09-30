# main/main.py

from fastapi import FastAPI
from routes.api_routes import router as api_router
from routes.chatbot_route import router as chat_router

app = FastAPI()

# Include the API routes
app.include_router(api_router)
app.include_router(chat_router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

