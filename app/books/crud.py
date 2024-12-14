from typing import List
from sqlalchemy import Result, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.books.schema import CreateBook
from app.core.sql_models import BookAlcemyModel


async def create_book(book_in: CreateBook,
                      session: AsyncSession) -> BookAlcemyModel:
    
    new_book = BookAlcemyModel(**book_in.model_dump())
    session.add(new_book)
    await session.commit()
    return new_book


async def get_book(id: int,
                   session: AsyncSession) -> BookAlcemyModel | None:
    
    book = await session.get(BookAlcemyModel, id)
    return book


async def get_all_books(session: AsyncSession) -> List[BookAlcemyModel]:

    stmt = select(BookAlcemyModel)
    result: Result = await session.execute(stmt)
    books = result.scalars().all()

    return list(books)


async def put_book(id: int,
                   book_in: CreateBook,
                   session: AsyncSession) -> BookAlcemyModel | None:
    
    new_values: dict = book_in.model_dump()
    book = update(BookAlcemyModel). where(BookAlcemyModel.id==id).values(new_values)
    await session.execute(book)
    await session.commit()
    return await session.get(BookAlcemyModel, id)


async def delete_book(id: int,
                      session: AsyncSession) -> None:
    
    book = await session.get(BookAlcemyModel, id)
    await session.delete(book)
    await session.commit()