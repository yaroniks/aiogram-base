from config import settings
from app.utils.enums import *
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base, async_session
from sqlalchemy import select, update, delete, func
from sqlalchemy import BIGINT, String, Enum, ForeignKey, Boolean


class Chat(Base):
    __tablename__ = 'chats'

    id = mapped_column(BIGINT, primary_key=True)

    @staticmethod
    async def add_chat(chat_id: int) -> None:
        async with async_session() as session:
            chat = await session.scalar(select(Chat).where(Chat.id == chat_id))
            if not chat:
                session.add(Chat(id=chat_id))
                await session.commit()
