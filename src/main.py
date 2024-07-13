from fastapi import FastAPI
from sqladmin import Admin, ModelView
from .database import engine, Base
from .cors import add_cors
from src.auth.models import User
from src.quizzes.models import Quiz
from src.questions.models import Question
from src.answers.models import Answer
from src.auth.routers import router as user_router
# from src.quizzes.routers import router as quizzes_router
# from src.questions.routers import router as questions_router
# from src.answers.routers import router as answers_router

Base.metadata.create_all(engine)

app = FastAPI()
add_cors(app)
admin = Admin(app, engine)

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username]

class QuizAdmin(ModelView, model=Quiz):
    column_list = [Quiz.id, Quiz.title, Quiz.questions]

class QuestionAdmin(ModelView, model=Question):
    column_list = [Question.id, Question.text, Question.answers]

class AnswerAdmin(ModelView, model=Answer):
    column_list = [Answer.id, Answer.text, Answer.is_correct]

admin.add_view(UserAdmin)
admin.add_view(QuizAdmin)
admin.add_view(QuestionAdmin)
admin.add_view(AnswerAdmin)

app.include_router(user_router, tags=["User"])

@app.get("/root")
def root():
    return "Hello world"