from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.database import Base
import uuid

class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True, unique=True, nullable=True)
    title = Column(String, index=True, nullable=False)
    questions = relationship("Question", back_populates="quiz")

    def __repr__(self):
        return f"{self.title}, id = {self.id}"