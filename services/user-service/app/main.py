from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models import Profile
from app.schemas import ProfileCreate, ProfileResponse
from app.utils import get_current_email

app = FastAPI(title="CloudForge User Service")

Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "user-service healthy"}


@app.post("/profiles", response_model=ProfileResponse)
def create_profile(
    profile: ProfileCreate,
    db: Session = Depends(get_db),
    email: str = Depends(get_current_email),
):
    new_profile = Profile(
        email=profile.email,
        full_name=profile.full_name
    )

    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)

    return new_profile


@app.get("/profiles/me", response_model=ProfileResponse)
def get_my_profile(
    db: Session = Depends(get_db),
    email: str = Depends(get_current_email),
):
    profile = db.query(Profile).filter(Profile.email == email).first()
    return profile
