from typing import List
from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.borrows.schema import CreateBorrows
from app.core.sql_models import BorrowAlchemyModels


async def create_borrows(borrows_in: CreateBorrows,
                         session: AsyncSession) -> BorrowAlchemyModels:
    
    new_borrows = BorrowAlchemyModels(**borrows_in.model_dump())
    session.add(new_borrows)
    await session.commit()
    return new_borrows


async def get_all_borrows(session: AsyncSession) -> List[BorrowAlchemyModels]:

    stmt = select(BorrowAlchemyModels)
    result: Result = await session.execute(stmt)
    borrows = result.scalars().all()
    return list(borrows)


async def get_borrows(id: int,
                      session: AsyncSession) -> BorrowAlchemyModels | None:
    
    borrow = await session.get(BorrowAlchemyModels, id)
    return borrow