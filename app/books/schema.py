from pydantic import BaseModel, ConfigDict, Field

from app.authors.schema import Author


class CreateBook(BaseModel):

    title: str
    description: str
    author_id: int = Field(..., gt=0)
    available_copies: int = Field(..., gt=-1)
    def __str__(self):
        return f"{self.__class__.__name__} title={self.title!r}, author_id={self.author_id}, available_copies={self.available_copies})"

    def __repr__(self):
        return str(self)


class Book(CreateBook):

    id: int
    author: Author

    model_config = ConfigDict(from_attributes=True)


class BookBorrow(CreateBook):

    id: int