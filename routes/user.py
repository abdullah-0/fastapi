from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.dependency import get_db, get_auth_user
from models import User
from schemas import UserAuth, UserCreate, UserLogin, Token, RefreshToken
from schemas.user import UserDetail
from utils import get_password_hashed, create_tokens, verify_password
from utils.user import decode_refresh_token

router = APIRouter()


@router.post("/register", response_model=UserAuth, status_code=201)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hashed(user.password)
    db_user = User(
        email=user.email,
        password=hashed_password,
        first_name=user.first_name,
        last_name=user.last_name,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    token = create_tokens(db_user.id)

    return {
        "user": db_user,
        "token": token,
    }


@router.post("/login", response_model=UserAuth)
async def login(request_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request_data.email).first()
    if not user or not verify_password(request_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    tokens = create_tokens(user.id)
    return {
        "user": user,
        "token": tokens,
    }


@router.post("/refresh", response_model=Token)
async def refresh_token(token: RefreshToken, db: Session = Depends(get_db)):
    payload = decode_refresh_token(token.refresh)
    user_id = payload.get("sub")

    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token"
        )

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found"
        )

    return create_tokens(user.id)


@router.get("/me", response_model=UserDetail)
async def read_user_me(current_user: User = Depends(get_auth_user)):
    return current_user
