from datetime import date
from pydantic import BaseModel, ConfigDict, Field

from app.books.schema import BookBorrow


class BaseBorrows(BaseModel):
    """Базовый класс для возврата с общими атрибутами."""

    book_id: int = Field(
        ...,
        gt=0,
        description="ID возврата должен быть больше 0"
        )
    reader_name: str
    
    def __str__(self):
        return (
            f"{self.__class__.__name__} "
            f"book_id={self.book_id!r}, "
            f"reader_name={self.reader_name!r})"
            )

    def __repr__(self):
        return str(self)


class CreateBorrows(BaseBorrows):
    """Схема для создания записи о возврате."""
    pass


class Borrows(BaseBorrows):
    """Схема для отображения полной информации о возврате"""

    id: int
    book: BookBorrow
    borrow_date: date

    model_config = ConfigDict(from_attributes=True)


class ReturnBorrows(Borrows):
    """Схема для выдачи с датой после возврата"""

    return_date: date

    model_config = ConfigDict(from_attributes=True)
