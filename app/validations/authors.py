from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.sql_models import AuthorAlchemyModel


async def validate_author(id: int,
                          session: AsyncSession) -> AuthorAlchemyModel:
    author = await session.get(AuthorAlchemyModel, id)
    if not author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Author with id {id} not found")
    return author