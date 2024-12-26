from typing import List
from sqlalchemy import Result, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.schemas.books import CreateBook
from app.core.sql_models import BookAlchemyModel
from app.validations.authors import validate_author
from app.validations.books import validate_book


async def create_book(
    book_in: CreateBook,
    session: AsyncSession
) -> BookAlchemyModel:
    """Создание записи информации о книге."""

    stmt = await validate_author(id=book_in.author_id, session=session)
    new_book = BookAlchemyModel(**book_in.model_dump())

    session.add(new_book)

    await session.commit()

    new_book.author = stmt
    
    return new_book


async def get_book(
    id: int,
    session: AsyncSession
) -> BookAlchemyModel:
    
    book = await validate_book(id=id, session=session)
    return book


async def get_all_books(session: AsyncSession) -> List[BookAlchemyModel]:

    stmt = select(BookAlchemyModel).options(joinedload(BookAlchemyModel.author))
    result: Result = await session.execute(stmt)
    books = result.scalars().all()

    return list(books)


async def put_book(
    id: int,
    book_in: CreateBook,
    session: AsyncSession
) -> BookAlchemyModel:
    
    await validate_book(id=id, session=session)
    await validate_author(id=book_in.author_id, session=session)
    
    new_values: dict = book_in.model_dump()
    book = (
        update(BookAlchemyModel)
        .where(BookAlchemyModel.id==id)
        .values(new_values)
        )
    
    await session.execute(book)
    await session.commit()

    return await validate_book(id=id, session=session)


async def delete_book(id: int,
                      session: AsyncSession) -> None:
    
    book = await validate_book(id=id, session=session)
    
    await session.delete(book)
    await session.commit()
    