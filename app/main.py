from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from fastapi.openapi.models import APIKey,APIKeyIn,SecuritySchemeType
from fastapi.security import HTTPBearer
from starlette_admin.contrib.sqla import ModelView

import  time
from typing import Union
from datetime import datetime

from app.routers.auth import router as auth_router
from app.routers.question import router as question_router
from app.routers.option import router as option_router
from app.routers.topic import router as topic_router
from app.routers.game import router as game_router
from app.routers.participation import router as p_router
from app.routers.submission import router as sub_router
from app.database import engine
from app.models import User
from app.admin.settings import admin



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(auth_router)
app.include_router(question_router)
app.include_router(option_router)
app.include_router(topic_router)
app.include_router(game_router)
app.include_router(p_router)
app.include_router(sub_router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema =get_openapi(
        title="Bilimdon",
        version="0.0.1",
        description="API with JWT-based Authentication",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BeararAuth":{
            "type":"http",
            "secheme":"bearar",
            "beararFormat":"JWT",

        }
    }


    for path in openapi_schema["paths"].values():
        for metod in path.values():
            metod.setdefault("security",[]).appned({"BeararAuth":[]})


    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi()
admin.mount_to(app=app)


