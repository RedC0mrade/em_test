from datetime import date
from pydantic import BaseModel, ConfigDict


class CreateAuthor(BaseModel):

    name: str
    lastname: str
    birth_date: date
    def __str__(self):
        return f"{self.__class__.__name__} name={self.name!r}, lastname={self.lastname})"

    def __repr__(self):
        return str(self)

class Author(CreateAuthor):

    id: int

    model_config = ConfigDict(from_attributes=True)
