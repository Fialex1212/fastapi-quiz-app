from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base
import uuid

class Question(Base):
    __tablename__ = "questions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True, unique=True, nullable=True)
    text = Column(String, index=True, nullable=False)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    quiz = relationship("Quiz", back_populates="questions")
    answers = relationship("Answer", back_populates="question")

    def __repr__(self):
        return f"{self.text}, id = {self.id}"