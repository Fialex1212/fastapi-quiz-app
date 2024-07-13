from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base
import uuid

class Answer(Base):
    __tablename__ = "answers"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True, unique=True, nullable=True)
    text = Column(String, index=True, nullable=False)
    is_correct = Column(Boolean, index=True, default=False, nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"))
    question = relationship("Question", back_populates="answers")

    def __repr__(self):
        return f"{self.text}, id = {self.id}"