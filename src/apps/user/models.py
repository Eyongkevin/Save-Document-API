from datetime import datetime
from uuid import uuid4

import bcrypt
from sqlalchemy import UUID, Boolean, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from src.db import db
from src.utils import generate_password_hash


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    public_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True), default=uuid4, unique=True, index=True, nullable=False
    )
    username: Mapped[str] = mapped_column(
        String(200), index=True, unique=True, nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(200), index=True, unique=True, nullable=False
    )
    password: Mapped[str] = mapped_column(String(300))
    active: Mapped[bool] = mapped_column(Boolean(), default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now()
    )
    modified_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now()
    )

    def __init__(
        self,
        username: str,
        email: str,
        password: str,
    ) -> None:
        """
        Use regex to validate these paramters
        - username: a single word
        - email: true email
        - password: max 8 chars, combination of letters, digits, special chars and upper cases.
        """
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.modified_at = datetime.utcnow()
