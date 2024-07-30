from .schemas import UserRequest,UserResponse
from .models import User
from .database import SessionLocal

async def create_user(user : UserRequest) -> UserResponse:
    db = SessionLocal()
    db_user = User(name=user.name, email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh()
