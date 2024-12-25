from datetime import date
from pydantic import BaseModel, ConfigDict


class BaseAuthor(BaseModel):
    """Базовый класс для автора с основными атрибутами."""

    name: str
    lastname: str
    birth_date: date
    def __str__(self):
        return (
            f"{self.__class__.__name__} "
            f"name={self.name!r}, "
            f"lastname={self.lastname!r})"
            )

    def __repr__(self):
        return str(self)


class CreateAuthor(BaseAuthor):
    """Схема для создания записи о авторе."""
    pass


class Author(BaseAuthor):
    """Схема отображения полной информации об авторе."""

    id: int

    model_config = ConfigDict(from_attributes=True)
