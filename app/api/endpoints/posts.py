import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app.api.dependecies import get_async_session
from app.api.endpoints.users import current_active_user
from app.api.utils import generate_id
from app.crud.posts import crud_posts
from app.models import User
from app.schemas.posts import PostRead, PostCreate, PostDB, PostUpdate

router = APIRouter()


@router.get('/', response_model=List[PostRead])
async def get_posts(db=Depends(get_async_session)):
    posts_db = await db.run_sync(crud_posts.get_multi)
    return posts_db


@router.get('/{id}', response_model=PostRead)
async def get_post_by_id(id: str, db=Depends(get_async_session)):
    post_db = await db.run_sync(crud_posts.get, id)

    if not post_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No such id")

    return post_db


@router.post('/create', response_model=PostRead)
async def create_post(post: PostCreate, db=Depends(get_async_session), current_user: User = Depends(current_active_user)):
    post_new = PostDB(id=generate_id(),
                      title=post.title,
                      text=post.text,
                      creator_id=current_user.id,
                      created=datetime.datetime.now())

    post_db = await db.run_sync(crud_posts.create, obj_in=post_new)
    return post_db


@router.put('/update/{id}', response_model=PostRead)
async def update_post(id: str, post: PostUpdate, db=Depends(get_async_session)):
    post_db = await db.run_sync(crud_posts.get, id)

    if not post_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No such id")

    updated = await db.run_sync(crud_posts.update, db_obj=post_db, obj_in=post)

    return updated


@router.delete('/delete/{id}', response_model=PostRead)
async def delete_post(id: str, db=Depends(get_async_session)):
    post_db = await db.run_sync(crud_posts.get, id)

    if not post_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No such id")

    deleted = await db.run_sync(crud_posts.remove, id=id)

    return deleted