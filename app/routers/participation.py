from email.policy import default

from fastapi import  APIRouter, Depends, HTTPException

from app.dependencies import db_dep,current_user_dep,admin_user_dep
from app.schemas import ParticipationResponce,ParticipationCreate,ParticipationUpdate
from app.models import Participation



router = APIRouter(prefix="/participations",tags=["participations"])


@router.get("/",response_model=list[ParticipationResponce])
async def get_participation(
        db:db_dep,
        id:int
):
    return db.query(Participation).filter(Participation.id == id).first()

@router.post("/create/",response_model=ParticipationResponce)
async def create_participation(
        db:db_dep,
        current_user:current_user_dep,
        participation:ParticipationCreate
):
    db_participation = Participation(
        **participation.model_dump(exclude_unset=True),
        user_id = current_user.id
    )

    db.add(db_participation)
    db.commit()
    db.refresh(db_participation)

    return db_participation

#Update

@router.patch("/{id}/update",response_model=ParticipationResponce)
async def update_particitpation(
        db:db_dep,
        current_user:current_user_dep,
        participation:ParticipationUpdate

):
    participation_obj = db.query(Participation).filter(Participation.id == id).first()

    if not participation_obj:
        raise HTTPException(
            status_code=404,
            detail={
                "Particition with this id is not found."

            }
        )

    participation_obj.start_time = participation.start_time if participation.start_time else participation_obj.start_time
    participation_obj.end_time = participation.end_time if participation.end_time else participation_obj.end_time
    participation_obj.gained_score = participation.gained_score if participation.gained_score else participation_obj.gained_score


    db.commit()
    db.query(participation_obj)

    return participation_obj

@router.get("/{id}/submissions/")
async def participation_submissions(
        db:db_dep,
        current_user:current_user_dep

):

    pass

