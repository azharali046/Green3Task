from pydantic import BaseModel, validator, root_validator


class CreateAuthor(BaseModel):
    name: str

    @validator('name')
    def name_must_be_string(cls, v):
        if v.isdigit():
            raise ValueError('name must be a string value')
        return v.title()

    @validator('name')
    def name_not_be_empty(cls, v):
        if not v:
            raise ValueError('name must not be empty')
        return v.title()


class UpdateAuthor(BaseModel):
    name: str

    @validator('name')
    def name_must_be_string(cls, v):
        if v.isdigit():
            raise ValueError('name must be a string value')
        return v.title()

    @validator('name')
    def name_not_be_empty(cls, v):
        if not v:
            raise ValueError('name not be empty')
        return v.title()


class CreateBook(BaseModel):
    name: str
    author_id: int

    @validator('name')
    def name_must_be_string(cls, v):
        if v.isdigit():
            raise ValueError('name must be a string value')
        return v.title()

    @validator('author_id')
    def author_id_must_be_integer(cls, v):
        if not type(v) == int:
            raise ValueError('author id must be an integer value')
        return v

    @validator('author_id')
    def author_id_must_not_be_empty(cls, v):
        if v is None:
            raise ValueError('author id must not be empty')
        return v

    @validator('name')
    def name_not_be_empty(cls, v):
        if not v:
            raise ValueError('name must not be empty')
        return v.title()


class UpdateBook(BaseModel):
    name: str
    author_id: int

    @validator('name')
    def name_must_be_string(cls, v):
        if v.isdigit():
            raise ValueError('must be a string value')
        return v.title()

    @validator('author_id')
    def author_id_must_be_integer(cls, v):
        if not type(v) == int:
            raise ValueError('author id must be an integer value')
        return v

    @validator('author_id')
    def author_id_must_not_be_empty(cls, v):
        if v is None:
            raise ValueError('author id must not be empty')
        return v

    @validator('name')
    def name_not_be_empty(cls, v):
        if not v:
            raise ValueError('name not be empty')
        return v.title()
