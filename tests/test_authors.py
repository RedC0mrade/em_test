# tests/test_authors.py
import pytest
from sqlalchemy import select
from app.authors.schema import CreateAuthor
from app.authors.crud import (create_author,
                              get_all_authors,
                              put_author,
                              delete_author)
from app.core.sql_models import AuthorAlchemyModel


@pytest.mark.asyncio
async def test_create_author(session):
    # Данные для нового автора
    author_data = CreateAuthor(name="John", lastname="Doe", birth_date="1980-01-01")
    
    # Создаем автора
    author = await create_author(author_in=author_data, session=session)
    
    # Проверяем, что автор был добавлен в базу
    result = await session.execute(select(AuthorAlchemyModel).filter_by(name="John", lastname="Doe"))
    author_in_db = result.scalar_one_or_none()
    
    assert author_in_db is not None
    assert author_in_db.name == "John"
    assert author_in_db.lastname == "Doe"


@pytest.mark.asyncio
async def test_create_author(session):
    author_data = CreateAuthor(name="John", lastname="Doe", birth_date="1980-01-01")
    author = await create_author(author_in=author_data, session=session)
    
    result = await session.execute(select(AuthorAlchemyModel).filter_by(name="John", lastname="Doe"))
    author_in_db = result.scalar_one_or_none()
    
    assert author_in_db is not None
    assert author_in_db.name == "John"
    assert author_in_db.lastname == "Doe"


@pytest.mark.asyncio
async def test_get_all_authors(session):
    # Создаем несколько авторов
    author_data1 = CreateAuthor(name="John", lastname="Doe", birth_date="1980-01-01")
    author_data2 = CreateAuthor(name="Jane", lastname="Smith", birth_date="1990-02-02")
    
    await create_author(author_in=author_data1, session=session)
    await create_author(author_in=author_data2, session=session)
    
    # Получаем всех авторов
    authors = await get_all_authors(session=session)
    
    assert len(authors) == 2
    assert authors[0].name == "John"
    assert authors[1].name == "Jane"


@pytest.mark.asyncio
async def test_put_author(session):
    # Создаем автора
    author_data = CreateAuthor(name="John", lastname="Doe", birth_date="1980-01-01")
    author = await create_author(author_in=author_data, session=session)
    
    # Обновляем автора
    updated_data = CreateAuthor(name="John", lastname="Updated", birth_date="1985-05-05")
    updated_author = await put_author(id=author.id, author_in=updated_data, session=session)
    
    assert updated_author.lastname == "Updated"
    assert updated_author.birth_date == "1985-05-05"


@pytest.mark.asyncio
async def test_delete_author(session):
    # Создаем автора
    author_data = CreateAuthor(name="John", lastname="Doe", birth_date="1980-01-01")
    author = await create_author(author_in=author_data, session=session)
    
    # Удаляем автора
    await delete_author(id=author.id, session=session)
    
    # Проверяем, что автор был удален
    result = await session.execute(select(AuthorAlchemyModel).filter_by(id=author.id))
    deleted_author = result.scalar_one_or_none()
    
    assert deleted_author is None