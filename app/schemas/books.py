from pydantic import BaseModel, ConfigDict, Field
from app.authors.schema import Author

class BaseBook(BaseModel):
    """Базовый класс для книг с общими атрибутами."""

    title: str
    description: str
    author_id: int = Field(
        ...,
        gt=0,
        description="ID автора должен быть больше 0"
        )
    available_copies: int = Field(
        ..., 
        ge=0, 
        description="Количество доступных копий не может быть отрицательным"
        )

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"title={self.title!r}, author_id={self.author_id}, "
            f"available_copies={self.available_copies})"
        )

    def __repr__(self):
        return str(self)


class CreateBook(BaseBook):
    """Схема для создания книги."""

    pass


class Book(BaseBook):
    """Схема для отображения полной информации о книге."""

    id: int
    author: Author

    model_config = ConfigDict(from_attributes=True)


class BookBorrow(BaseBook):
    """Схема для выдачи книги."""
    
    id: int

    