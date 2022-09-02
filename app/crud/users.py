from app.crud.generic import CRUDBase
from app.models import User
from app.schemas.users import UserDB, UserUpdate


class CRUDUser(CRUDBase[User, UserDB, UserUpdate]):
    pass


crud_users = CRUDUser(User)
