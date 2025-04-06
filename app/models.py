from sqlalchemy import String, Date, DateTime, Boolean, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from datetime import datetime, date, timezone

from typing import Optional, List

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column( unique=True)
    hashed_password: Mapped[str] = mapped_column(String(128))
    username: Mapped[str] = mapped_column(String(32))
    first_name: Mapped[str] = mapped_column(String(32))
    last_name: Mapped[str] = mapped_column(String(32))
    birthdate: Mapped[Optional[date]] = mapped_column(Date)
    joined_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    is_activate: Mapped[bool] = mapped_column( default=True)
    is_staff: Mapped[bool] = mapped_column( default=False)
    is_superuser: Mapped[bool] = mapped_column( default=False)



class Topic(Base):
    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), unique=True)


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


    owner: Mapped["User"] = relationship(back_populates="owned_games")
    questions: Mapped[List["GameQuestion"]] = relationship(back_populates="game")




class GameQuestion(Base):
    __tablename__ = "game_questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int] = mapped_column(Integer, ForeignKey("games.id"))
    question_id: Mapped[int] = mapped_column(Integer, ForeignKey("questions.id"))


    game: Mapped["Game"] = relationship(back_populates="questions")
    question: Mapped["Question"] = relationship(back_populates="games")


class Question(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(String(1000), nullable=True)
    topic_id: Mapped[int] = mapped_column(Integer, ForeignKey("topics.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))

    # Relationships
    option_ids: Mapped[List["Option"]] = relationship(back_populates="question")
    games: Mapped[List["GameQuestion"]] = relationship(back_populates="question")


class Participation(Base):
    __tablename__ = "participations"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    game_id: Mapped[int] = mapped_column(Integer, ForeignKey("games.id"))
    start_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    end_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    gained_score: Mapped[int] = mapped_column(Integer, default=0)
    registered_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))


class Option(Base):
    __tablename__ = "options"

    id: Mapped[int] = mapped_column(primary_key=True)
    question_id: Mapped[int] = mapped_column(Integer, ForeignKey("questions.id"))
    title: Mapped[str] = mapped_column(String(100))
    is_correct: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))



class Submission(Base):
    __tablename__ = "submissions"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    question_id: Mapped[int] = mapped_column(Integer, ForeignKey("questions.id"))
    option_id: Mapped[int] = mapped_column(Integer, ForeignKey("options.id"))
    is_correct: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))

    # Relationships
    owner: Mapped["User"] = relationship(back_populates="submissions")
    question: Mapped["Question"] = relationship(back_populates="submissions")
    option: Mapped["Option"] = relationship(back_populates="submissions")
