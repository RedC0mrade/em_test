import uvicorn

from fastapi import FastAPI

from app.authors.views import authors
from app.books.views import books
from app.borrows.views import borrows


app = FastAPI()
app.include_router(authors)
app.include_router(books)
app.include_router(borrows)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
