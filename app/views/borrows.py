from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.borrows.schema import Borrows, CreateBorrows, ReturnBorrows
from app.core.engine import db_helper
from app.borrows import crud

borrows = APIRouter(prefix="/borrows", tags=["borrows"])

@borrows.post("/", response_model=Borrows)
async def create_borrows(borrows_in: CreateBorrows,
                         session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_borrows(borrows_in=borrows_in, session=session)


@borrows.get("/", response_model=list[Borrows])
async def get_all_borrows(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_all_borrows(session=session)


@borrows.get("/{id}", response_model=Borrows)
async def get_borrows(id: int,
                      session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_borrows(id=id, session=session)


@borrows.patch("/{id}/return", response_model=ReturnBorrows)
async def patch_borrows(id: int,
                        session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.patch_borrows(id=id, session=session)
