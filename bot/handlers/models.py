from bot.utils.database import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import (
    Integer,
    String
)


class ArticleModel(Base):
    __tablename__ = "articles"
    id: Mapped[int] = mapped_column(
        Integer, index=True, 
        primary_key=True, autoincrement=True
    )
    link: Mapped[str] = mapped_column(String)
    title: Mapped[str] = mapped_column(String)

class UserModel(Base):
    __tablename__ = "users"
    user_id: Mapped[int] = mapped_column(
        Integer, index=True, 
        primary_key=True, autoincrement=True
    )
    is_active: Mapped[bool] = mapped_column(default=True)
