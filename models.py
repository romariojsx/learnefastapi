from email.policy import default
from operator import index
from turtle import title
from sqlalchemy import Boolean, Column, Integer, String

from database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    complete = Column(Boolean, default=False)


class users(Base):
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    senhaHash = Column(str, default=False)
    role = Column(Boolean, default=False)
