import pytest

from app.authors.schema import CreateAuthor
from app.authors.crud import create_author, get_all_authors, delete_author
from app.core.sql_models import AuthorAlchemyModel


@pytest.mark.asyncio
async def test_create_author(session):

    author_data = CreateAuthor(name="Bill", lastname="Bob", birth_date="9999-99-99")
    author = await create_author(author_in=author_data, session=session)
    
    assert author.name == "Bill"
    assert author.lastname == "Bob"
    assert isinstance(author, AuthorAlchemyModel)


@pytest.mark.asyncio
async def test_get_all_authors(session):

    author_data1 = CreateAuthor(name="Bill", lastname="Bob", birth_date="9999-01-01")
    author_data2 = CreateAuthor(name="Tim", lastname="Sam", birth_date="0001-02-02")

    await create_author(author_in=author_data1, session=session)
    await create_author(author_in=author_data2, session=session)

    authors = await get_all_authors(session=session)
    
    assert len(authors) == 2
    assert authors[0].name == "Bill"
    assert authors[1].lastname == "Sam"



@pytest.mark.asyncio
async def test_delete_author(session):

    author_in = CreateAuthor(name="Bill", lastname="Bob", birth_date="1980-01-01")
    author = await create_author(author_in=author_in, session=session)

    result = await delete_author(id=author.id, session=session)

    assert result is None
    authors = await get_all_authors(session=session)
    assert len(authors) == 0
