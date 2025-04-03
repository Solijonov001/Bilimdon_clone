from sqlalchemy import  String,Date,DateTime

from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime, timezone
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id : Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password : Mapped[str] = mapped_column(String(128))
    username : Mapped[str] = mapped_column(String(32))
    first_name : Mapped[str] = mapped_column(String(32))
    last_name : Mapped[str] = mapped_column(String(32))
    birthday : Mapped[datetime] = mapped_column(Date)
    joinned_at : Mapped[bool] = mapped_column(DateTime,default=datetime.now(timezone.utc))
    is_activate : Mapped[bool] = mapped_column(default=True)
    is_staff : Mapped[bool] = mapped_column(default=False)
    is_superuser : Mapped[bool] =mapped_column(default=False)


