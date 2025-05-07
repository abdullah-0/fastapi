import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from core.config import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String(127), unique=True, index=True)
    password = Column(String())
    first_name = Column(String(63), nullable=False)
    last_name = Column(String(63), default="")
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    is_email_verified = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))
    updated_at = Column(
        DateTime,
        default=datetime.datetime.now(datetime.UTC),
        onupdate=datetime.datetime.now(datetime.UTC),
    )
    # Relations
    entities = relationship("models.entity.Entity", back_populates="user")