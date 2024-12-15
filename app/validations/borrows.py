from fastapi import HTTPException, status
from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.core.sql_models import BorrowAlchemyModel


async def validate_borrows(id: int,
                          session: AsyncSession) -> BorrowAlchemyModel:
    
    stmt = (select(BorrowAlchemyModel)
    .options(joinedload(BorrowAlchemyModel.book))
    .where(BorrowAlchemyModel.id == id))

    result: Result = await session.execute(stmt)
    borrows = result.scalar_one_or_none()    
    
    if not borrows:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Borrows with id {id} not found")
    return borrows