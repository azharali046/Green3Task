from pydantic import BaseModel, validator


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

