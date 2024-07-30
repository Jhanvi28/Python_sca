from fastapi import APIRouter, status, HTTPException
from .schemas import UserRequest, UserResponse
from .models import User

router = APIRouter()

@router.post("/webhook")
def create_webhook(body:any):
    print(body)


@router.post(
    "users",
    response_model=UserRequest,
    status_code=status.HTTP_201_CREATED
)
def create_user(user : UserRequest):
    pass

@router.get(
    "users",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK
)
def get_users():
    pass