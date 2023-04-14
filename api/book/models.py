from sqlalchemy import Column, ForeignKey, Integer, String, inspect
from sqlalchemy.orm import relationship

from api.author.models import Author
from database import Base


class Book(Base):
    """
     this table is used to create Book

    Columns
    **id**: integer value and primary key of the table
    **name**: name of the book
    **author_id**: foreign key (Relationship Table Author)

    Relationship
    **name**: author
    (book has one author)
    """
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=True, unique=True, index=True)
    author_id = Column(Integer, ForeignKey(Author.id, ondelete="CASCADE"), nullable=False)
    access = relationship(Author, foreign_keys=author_id)

    def toDict(self):
        """
        this function is used to change the model object to dict
        """
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
