from sqlalchemy import Column, Integer, String, inspect
from database import Base


class Author(Base):
    """
    this table is used to create author

    Columns
    **id**: integer value and primary key of the table
    **name**: name of the author
    """
    __tablename__ = "author"
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=True)

    def toDict(self):
        """
        this function is used to change the model object to dict
        """
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

