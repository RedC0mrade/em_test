from datetime import date
from sqlalchemy import CheckConstraint, Date, ForeignKey, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"
    
    id: Mapped[int] = mapped_column(primary_key=True)


class AuthorAlchemyModel(Base):
    __tablename__ = "authors"

    name: Mapped[str] = mapped_column(String(30), nullable=False)
    lastname: Mapped[str] = mapped_column(String(30), nullable=False)
    birth_date: Mapped[date] = mapped_column(nullable=False)
    books: Mapped[list["BookAlchemyModel"]] = relationship(back_populates="author",
                                                          cascade="all, delete-orphan")


class BookAlchemyModel(Base):
    __tablename__ = "books"

    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"), nullable=False)
    available_copies: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    author: Mapped["AuthorAlchemyModel"] = relationship(back_populates="books")
    borrows: Mapped[list["BorrowAlchemyModel"]] = relationship("BorrowAlchemyModel",
                                                               back_populates="book",
                                                               cascade="all, delete-orphan")


class BorrowAlchemyModel(Base):
    __tablename__ = "borrows"
 
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"), nullable=False)
    reader_name: Mapped[str] = mapped_column(String(30), nullable=False)
    borrow_date: Mapped[date] = mapped_column(nullable=False, default=date.today)
    return_date: Mapped[date] = mapped_column(nullable=True)
    book: Mapped["BookAlchemyModel"] = relationship("BookAlchemyModel", back_populates="borrows")
