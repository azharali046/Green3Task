from fastapi import APIRouter, Response, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from api.author.schemas import CreateAuthor, UpdateAuthor
from api.author.utils import save_author, get_authors, get_author_by_id, update_author_by_id, delete_author_by_id
from api.constants import response_body
from database_dependency import get_db

router = APIRouter()


@router.post('/authors',tags=['Author'])
def create_author(response: Response, author_schema: CreateAuthor, db: Session = Depends(get_db)):
    """
        save a new author
        - **name**: name of author
        - **201**: Successfully created
        - **422**: Validation Error
    """
    message, status_code = save_author(db=db, name=author_schema.name)
    response_body['message'] = message
    response_body['data'] = []
    response.status_code = status_code
    return JSONResponse(content=response_body, status_code=response.status_code)


@router.get('/authors',tags=['Author'])
def fetch_authors(response: Response, db: Session = Depends(get_db)):
    """
        fetch list of authors
    """
    authors_data = get_authors(db=db)
    response_body['message'] = ''
    response_body['data'] = jsonable_encoder(authors_data)
    response.status_code = 200
    return JSONResponse(content=response_body, status_code=response.status_code)


@router.get('/authors/{id}',tags=['Author'])
def fetch_authors_by_id(response: Response, id: int, db: Session = Depends(get_db)):
    """
        fetch author against author id
        - **id**: id of author
        - **200**: Successfully fetch
        - **422**: Validation Error
        - **404**: No record found

    """
    authors_data, status_code, = get_author_by_id(db=db, id=id)
    response_body['message'] = ''
    response_body['data'] = jsonable_encoder(authors_data)
    response.status_code = status_code
    return JSONResponse(content=response_body, status_code=response.status_code)


@router.patch('/authors/{id}',tags=['Author'])
def update_author(response: Response, id: int, author_schema: UpdateAuthor, db: Session = Depends(get_db)):
    """
            update author against author id
            - **id**: id of author
            - **name**: name of author
            - **200**: Successfully updated
            - **422**: Validation Error
            - **404**: No record found


    """
    message, status_code = update_author_by_id(db=db, id=id, name=author_schema.name)
    response_body['message'] = message
    response_body['data'] = []
    response.status_code = status_code
    return JSONResponse(content=response_body, status_code=response.status_code)


@router.delete('/authors/{id}',tags=['Author'])
def delete_author(response: Response, id: int, db: Session = Depends(get_db)):
    """
            delete author against author id
            - **id**: id of author
            - **200**: Successfully deleted
            - **422**: Validation Error
            - **404**: No record found
       """
    message, status_code = delete_author_by_id(db=db, id=id)
    response_body['message'] = message
    response_body['data'] = []
    response.status_code = status_code
    return JSONResponse(content=response_body, status_code=response.status_code)