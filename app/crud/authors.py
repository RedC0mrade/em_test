from typing import List
from sqlalchemy import Result, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.authors.schema import CreateAuthor
from app.core.sql_models import AuthorAlchemyModel
from app.validations.authors import validate_author


async def create_author(
    author_in: CreateAuthor,
    session: AsyncSession
) -> AuthorAlchemyModel:
    """Создаёт нового автора и сохраняет его в базе данных."""
    new_author = AuthorAlchemyModel(**author_in.model_dump())
    session.add(new_author)
    await session.commit()
    return new_author


async def get_all_authors(session: AsyncSession) -> List[AuthorAlchemyModel]:
    """Возвращает список всех авторов."""

    stmt = select(AuthorAlchemyModel)
    result: Result = await session.execute(stmt)
    
    return result.scalars().all()


async def get_author(
    id: int,
    session: AsyncSession
) -> AuthorAlchemyModel:
    """Возвращает автора по его ID, если он существует."""

    return await validate_author(id=id, session=session)


async def put_author(
    id: int,
    author_in: CreateAuthor,
    session: AsyncSession
) -> AuthorAlchemyModel:
    """Обновляет информацию об авторе по его ID."""

    await validate_author(id=id, session=session)
    updated_values = author_in.model_dump()
    stmt = (
        update(AuthorAlchemyModel)
        .where(AuthorAlchemyModel.id == id)
        .values(updated_values)
    )

    await session.execute(stmt)
    await session.commit()

    return await validate_author(id=id, session=session)


async def delete_author(
    id: int,
    session: AsyncSession
) -> None:
    """Удаляет автора по его ID."""
    author = await validate_author(id=id, session=session)
    await session.delete(author)
    await session.commit()
