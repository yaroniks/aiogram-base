from config import settings
from app.database.base import Base, async_session

from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import select, update, delete, func
from sqlalchemy import BIGINT, String, Enum, ForeignKey, Boolean


class Chat(Base):
    __tablename__ = 'chats'

    chat_id = mapped_column(BIGINT, primary_key=True, unique=True)

    @staticmethod
    async def add_chat(chat_id: int) -> None:
        """Добавить чат"""
        async with async_session() as session:
            chat = await session.scalar(select(Chat).where(Chat.chat_id == chat_id))
            if not chat:
                session.add(Chat(id=chat_id))
                await session.commit()

    @staticmethod
    async def get_chat(chat_id: int) -> Optional['Chat']:
        """Получить чат по ID"""
        async with async_session() as session:
            chat = await session.scalar(select(Chat).where(Chat.chat_id == chat_id))
            return chat
