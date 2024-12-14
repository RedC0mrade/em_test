from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.books import crud
from app.books.schema import Book, CreateBook
from app.core.engine import db_helper

books = APIRouter(prefix="/books", tags=["books"])

@books.post("/", response_model=Book, status_code=201)
async def create_book(book_in: CreateBook,
                      session: AsyncSession = Depends(db_helper.session_dependency)):    
    return await crud.create_book(book_in=book_in, session=session)


@books.get("/{id}", response_model=Book)
async def get_book(id: int,
                   session: AsyncSession = Depends(db_helper.session_dependency)):    
    return await crud.get_book(id=id, session=session)


@books.get("/", response_model=list[Book])
async def get_all_books(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_all_books(session=session)


@books.put("/{id}", response_model=Book | None)
async def put_book(id: int,
                   book_in: CreateBook,
                   session: AsyncSession = Depends(db_helper.session_dependency)):    
    return await crud.put_book(id=id, book_in=book_in, session=session)


@books.delete("/{id}", status_code=204)
async def delete_book(id: int,
                      session: AsyncSession = Depends(db_helper.session_dependency)):    
    return await crud.delete_book(id=id, session=session)
