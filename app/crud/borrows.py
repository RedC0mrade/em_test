from datetime import datetime
from typing import List
from fastapi import HTTPException, status
from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload


from app.borrows.schema import CreateBorrows
from app.core.sql_models import BorrowAlchemyModel
from app.validations.books import validate_book
from app.validations.borrows import validate_borrows


async def create_borrows(
    borrows_in: CreateBorrows,
    session: AsyncSession
) -> BorrowAlchemyModel:
    """Создание информации о получении книги."""
    
    book = await validate_book(id=borrows_in.book_id, session=session)
    
    if book.available_copies == 0:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=(
                f"The book with id {borrows_in.book_id} "
                f"is not available."
                )
            )
    book.available_copies -= 1
    session.add(book)

    new_borrows = BorrowAlchemyModel(**borrows_in.model_dump())
    session.add(new_borrows)

    await session.commit()

    return await validate_borrows(id=new_borrows.id, session=session)


async def get_all_borrows(session: AsyncSession) -> List[BorrowAlchemyModel]:

    stmt = (
        select(BorrowAlchemyModel)
        .options(joinedload(BorrowAlchemyModel.book)))
    result: Result = await session.execute(stmt)

    borrows = result.scalars().all()
    
    return list(borrows)


async def get_borrows(
    id: int,
    session: AsyncSession
) -> BorrowAlchemyModel:

    return await validate_borrows(id=id, session=session)


async def patch_borrows(
    id: int,
    session: AsyncSession
) -> BorrowAlchemyModel:
    """Исправление информации о получении книги"""
    
    borrow = await validate_borrows(id=id, session=session)
    if borrow.return_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                f"The book has already been returned in {borrow.return_date}."
                )
        )
    borrow.return_date = datetime.now().date()
    session.add(borrow)
    
    book = await validate_book(id=borrow.book_id, session=session)
    book.available_copies += 1
    session.add(book)

    await session.commit()
    return borrow
