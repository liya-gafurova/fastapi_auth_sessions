from fastapi import FastAPI

from app.api.dependecies import create_db_and_tables
from app.api.endpoints.posts import router as posts_router
from app.api.endpoints.users import router as users_router, fastapi_users, authentication_backend
from app import models
from app.db.session import engine
from app.schemas.users import UserDB, UserCreate

app = FastAPI()

app.include_router(posts_router, prefix='/posts', tags=['Posts'])
app.include_router(users_router, prefix='/users', tags=['Users'])


app.include_router(fastapi_users.get_register_router(UserDB, UserCreate))

app.include_router(fastapi_users.get_auth_router(authentication_backend), prefix='/auth', tags=['Login/Logout'])


@app.on_event('startup')
async def on_startapp():
    await create_db_and_tables()