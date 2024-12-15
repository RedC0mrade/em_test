from typing import List
from sqlalchemy import Result, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.authors.schema import CreateAuthor
from app.core.sql_models import AuthorAlchemyModel
from app.validations.authors import validate_author


async def create_author(author_in: CreateAuthor,
                        session: AsyncSession) -> AuthorAlchemyModel:
    
    new_author = AuthorAlchemyModel(**author_in.model_dump())
    session.add(new_author)
    await session.commit()
    return new_author


async def get_all_authors(session: AsyncSession) -> List[AuthorAlchemyModel]:

    stmt = select(AuthorAlchemyModel)
    result: Result = await session.execute(stmt)
    authors = result.scalars().all()
    return list(authors)


async def get_author(id: int, session: AsyncSession) -> AuthorAlchemyModel:

    author = await validate_author(id=id, session=session)
    return author


async def put_author(id: int, author_in: CreateAuthor, session: AsyncSession) -> AuthorAlchemyModel:

    await validate_author(id=id, session=session)
    new_values: dict = author_in.model_dump()
    author = update(AuthorAlchemyModel).where(AuthorAlchemyModel.id==id).values(new_values)
    await session.execute(author)
    await session.commit()
    return await validate_author(id=id, session=session)


async def delete_author(id: int, session: AsyncSession) -> None:

    author = await validate_author(id=id, session=session)
    await session.delete(author)
    await session.commit()
