from pydantic import BaseModel, Field

EMAIL_REGEX = (
    r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
)

PASSWORD_REGEX = (

    'Password must be at least 8 characters long and contain '
    'at least one uppercase letter, one lowercase letter, '
    'one digit, and one special character.'

    r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
)

class UserRequest(BaseModel):
    id: int
    name: str
    email: str = Field(regex=EMAIL_REGEX)
    password: str = Field(regex=PASSWORD_REGEX)

class UserResponse(BaseModel):
    name: str
    email: str