# main/routes/api_routes.py

from fastapi import APIRouter

from api.api_functions import get_test2_response

router = APIRouter()

@router.get("/test")
async def test_endpoint():
    return {"message": "This is a test endpoint!"}


@router.get("/api/test2")
async def test2():
    response = get_test2_response()
    return await response
