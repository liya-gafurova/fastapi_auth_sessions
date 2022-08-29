from app.crud.generic import CRUDBase
from app.models import Post
from app.schemas.posts import PostDB, PostUpdate


class CRUDPost(CRUDBase[Post, PostDB, PostUpdate]):
    pass


crud_posts = CRUDPost(Post)
