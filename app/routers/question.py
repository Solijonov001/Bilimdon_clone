from fastapi import APIRouter,HTTPException

from app.models import Question
from app.dependencies import db_dep,current_user_dep
from app.schemas import QuestionResponse,QuestionCreate,QuestionUpdate


router =  APIRouter(prefix="/questions",tags=["questions"])

@router.get("/",response_model=list[QuestionResponse])
async def get_questions(db:db_dep):
    return db.query().all()

@router.get("/{id}",response_model=QuestionResponse)
async def get_question(id:int,db:db_dep):
    question = db.query(Question).filter(Question.id == id).first()


    if not question:
        raise HTTPException(
            status_code=404,
            detail="Question not found."
            )
    return question


@router.post("/create/",response_model=QuestionResponse)
async def create_question(
        question:QuestionCreate,
        db:db_dep,
        current_user: current_user_dep
):
        db_question = Question(
            **question.model_dump(),
            owner_id = current_user.id
        )

        db.add(db_question)
        db.commit()
        db.refresh(db_question)

        return db_question


@router.put("/update/{id}",response_model=QuestionResponse)
async def update_question(
        id: int,
        question:QuestionUpdate,
        db:db_dep
):
    db_question = db.query(Question).filter(Question.id == id).first()

    if not db_question:
        raise HTTPException(
        status_code=404,
         detail="Queation not found."
            )

    db_question.title = question.title if question.title else db_question.title
    db_question.desciption = question.decription if question.decription else  db_question.desciption
    db_question.topic_id= question.topic_id if question.topic_id else db_question.topic_id

    db.commit()
    db.refresh(db_question)

    return db_question


@router.delete("/delete/{id}")
async def delete_question(id:int,db: db_dep):
    db_question = db.query(Question).filter(Question.id == id).first()


    if not db_question:
        raise HTTPException(
            status_code=404,
            detail="Question not found."
        )

    db.delete(db_question)
    db.commit()

    return {
        "question_id":id,
        "massage":"Question not found."

    }

# @router.get("/{id}/options",response_model=QuestionWithOptionsResponse)
# async def get_qestion_with_options(id:int,db:db_dep)
#     pass
#




















