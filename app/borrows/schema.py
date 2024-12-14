from datetime import date
from pydantic import BaseModel, Field


class CreateBorrows(BaseModel):

    book_id: int = Field(..., gt=0)
    reader_name: str

    def __str__(self):
        return f"{self.__class__.__name__} book_id={self.book_id!r}, reader_name={self.reader_name!r})"

    def __repr__(self):
        return str(self)
    

class Borrows(CreateBorrows):

    id: int
    borrow_date: date


class ReturnBorrows(Borrows):

    return_date: date
