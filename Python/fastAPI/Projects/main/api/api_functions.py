# api/api_functions.py

from fastapi import HTTPException

async def get_test2_response():
    # Example response for the test2 route
    return {"message": "This is the response from the test2 API function."}
