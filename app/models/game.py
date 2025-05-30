
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String,DateTime,Date,Integer,Boolean,ForeignKey

from datetime import datetime
from typing import List

from app.database import Base



class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(1000))
    topic_id: Mapped[int] = mapped_column(Integer, ForeignKey("topics.id"))
    score: Mapped[int] = mapped_column(Integer, default=0)
    start_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    owner: Mapped["User"] = relationship("User", back_populates="owned_games")  # User bilan bog'lanish
    questions: Mapped[List["GameQuestion"]] = relationship(back_populates="game")  # GameQuestion bilan bog'lanish
    topic: Mapped["Topic"] = relationship("Topic", back_populates="games")  # Topic bilan bog'lanish
    submissions: Mapped["Submission"] = relationship("Submission", back_populates="game")  # Submission bilan bog'lanish
    participations: Mapped[List["Participation"]] = relationship(back_populates="game")  # Participation bilan bog'lanish


class GameQuestion(Base):
    __tablename__ = "game_questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int] = mapped_column(Integer, ForeignKey("games.id"))
    question_id: Mapped[int] = mapped_column(Integer, ForeignKey("questions.id"))

    question: Mapped["Question"] = relationship(back_populates="games")  # Question bilan bog'lanish
    game: Mapped["Game"] = relationship(back_populates="questions")  # Game bilan bog'lanish
