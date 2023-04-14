from typing import Optional

from fastapi import APIRouter, Response, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from api.constants import response_body
from api.book.schemas import CreateBook, UpdateBook
from api.book.utils import save_book, get_books, get_book_by_id, update_book_by_id, delete_book_by_id
from database_dependency import get_db

router = APIRouter()


@router.post('/books',tags=['Book'])
def create_book(response: Response, book_schema: CreateBook, db: Session = Depends(get_db)):
    """
        save a new book
        - **name**: unique name of book
       - **201**: Successfully created
       - **422**: Validation Error
    """
    message, status_code = save_book(db=db, name=book_schema.name, author_id=book_schema.author_id)
    response_body['message'] = message
    response_body['data'] = []
    response.status_code = 201
    return JSONResponse(content=response_body, status_code=response.status_code)


@router.get('/books',tags=['Book'])
def fetch_books(response: Response, author_id: Optional[int] = None, db: Session = Depends(get_db)):
    """
            fetch list of books
            - **author_id**: id of author Optional
    """
    books_data = get_books(db=db, author_id=author_id)
    response_body['message'] = ''
    response_body['data'] = jsonable_encoder(books_data)
    response.status_code = 200
    return JSONResponse(content=response_body, status_code=response.status_code)


@router.get('/books/{id}',tags=['Book'])
def fetch_books_by_id(response: Response, id: int, db: Session = Depends(get_db)):
    """
            fetch book against book id
            - **id**: id of book
            - **200**: Successfully fetch
            - **422**: Validation Error
            - **404**: No record found
    """
    books_data, status_code, = get_book_by_id(db=db, id=id)
    response_body['message'] = ''
    response_body['data'] = jsonable_encoder(books_data)
    response.status_code = status_code
    return JSONResponse(content=response_body, status_code=response.status_code)


@router.patch('/books/{id}',tags=['Book'])
def update_book(response: Response, id: int, book_schema: UpdateBook, db: Session = Depends(get_db)):
    """
            update book against book id
            - **id**: id of book
            - **name**: name of book
            - **author_id**: id of author
            - **200**: Successfully updated
            - **422**: Validation Error
            - **404**: No record found
      """
    message, status_code = update_book_by_id(db=db, id=id, name=book_schema.name, author_id=book_schema.author_id)
    response_body['message'] = message
    response_body['data'] = []
    response.status_code = status_code
    return JSONResponse(content=response_body, status_code=response.status_code)


@router.delete('/books/{id}',tags=['Book'])
def delete_book(response: Response, id: int, db: Session = Depends(get_db)):
    """
            delete book against book id
            - **id**: id of book
            - **200**: Successfully deleted
            - **422**: Validation Error
            - **404**: No record found
    """
    message, status_code = delete_book_by_id(db=db, id=id)
    response_body['message'] = message
    response_body['data'] = []
    response.status_code = status_code
    return JSONResponse(content=response_body, status_code=response.status_code)