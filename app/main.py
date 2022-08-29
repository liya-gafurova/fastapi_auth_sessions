from fastapi import FastAPI

from app.api.endpoints.posts import router
from app import models
from app.db.session import engine


models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(router)

