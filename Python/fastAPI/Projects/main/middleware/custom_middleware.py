# main/middleware/custom_middleware.py

from fastapi import Request, FastAPI

class CustomMiddleware:
    def __init__(self, app: FastAPI):
        self.app = app

    async def __call__(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Custom-Header"] = "My Custom Value"
        return response

# In main.py, you can include this middleware
from middleware.custom_middleware import CustomMiddleware
app.add_middleware(CustomMiddleware)
