import uuid

from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from app.models import User
from app.api.dependecies import get_user_manager, get_database_strategy
from fastapi_users.authentication import CookieTransport, AuthenticationBackend

router = APIRouter()

# @router.post('/register', response_model=UserRead)
# async def register_user(user: UserCreate, db=Depends(get_session)):
#
#     user_db: UserDB = UserDB(
#         username=user.username,
#         email=user.email,
#         password = hash_password(user.password),
#         id=generate_id(),
#         registered=datetime.datetime.now(),
#
#     )
#     created = crud_users.create(db=db, obj_in=user_db)
#
#     return created
#
#

"""
/login
/logout


"""


# User Manager

# Transport - Cookie

transport_cookie = CookieTransport()

# Strategy


# Auth Backend

authentication_backend = AuthenticationBackend(
    name="cookie",
    transport=transport_cookie,
    get_strategy=get_database_strategy
)

# users FastAPI app
fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [authentication_backend])

current_active_user = fastapi_users.current_user(active=True)
