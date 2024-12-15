from fastapi import HTTPException, status
from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.core.sql_models import BookAlchemyModel


async def validate_book(id: int,
                          session: AsyncSession) -> BookAlchemyModel:
    
    stmt = (select(BookAlchemyModel)
    .options(joinedload(BookAlchemyModel.author))
    .where(BookAlchemyModel.id == id))

    result: Result = await session.execute(stmt)
    book = result.scalar_one_or_none()

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Book with id {id} not found")
    return book
    