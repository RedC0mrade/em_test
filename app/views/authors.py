from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.authors import crud
from app.schemas.authors import CreateAuthor, Author
from app.core.engine import db_helper


authors = APIRouter(prefix="/authors", tags=["authors"])


@authors.post("/", response_model=Author, status_code=201)
async def create_author(author_in: CreateAuthor,
                    session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_author(author_in=author_in, session=session)


@authors.get("/", response_model=list[Author])
async def get_all_authors(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_all_authors(session=session)


@authors.get("/{id}", response_model=Author)
async def get_author(id: int,
                     session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_author(id=id, session=session)


@authors.put("/{id}", response_model=Author)
async def put_author(id: int,
                     author_in: CreateAuthor,
                     session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.put_author(id=id, author_in=author_in, session=session)


@authors.delete("/{id}", status_code=204)
async def delete_author(id: int,
                        session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.delete_author(id=id, session=session)
