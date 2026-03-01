from pydantic import BaseModel


class ProfileCreate(BaseModel):
    email: str
    full_name: str


class ProfileResponse(BaseModel):
    id: int
    email: str
    full_name: str

    class Config:
        orm_mode = True
