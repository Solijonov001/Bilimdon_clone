from pydantic import BaseModel

from datetime import datetime



class QuestionResponse(BaseModel):
    id : int
    ower_id: int
    title: str
    description :str | None = None
    create_at: datetime
    topic_id: int
    upatade_at: datetime

    model_config = {
        "from_attributes":True,
        "json_schem_extra": {
            "exmple": {
                "id":1,
                "owner_id":1,
                "title":"Question 1",
                "desription":"Question 1 description",
                "topic_id":1,
                "cerate_at": "2021-10-01T00:00:00",
                "update_at":"2021-01-01T00:00:00"

            }
        }
    }

class QuestionCreate(BaseModel):
    title: str
    description: str | None = None
    topic_id: int


class QuestionUpdate(BaseModel):
    title:str
    depcription: str | None = None
    topic_id: int | None = None

