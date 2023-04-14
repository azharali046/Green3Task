from sqlalchemy.exc import IntegrityError

from api.author.utils import get_author_by_id
from api.constants import no_record_found, save_book_msg, \
    update_book_msg, delete_book_msg, save_book_failure_msg, author_not_exist
from api.book.models import Book


def save_book(db, name, author_id):
    """

    :param db:
    :param name:
    :param author_id:
    :return:
    """
    """
    first check author validation either author exist or not
    """
    author_status = get_author_by_id(db=db, id=author_id)[1]
    if author_status == 200:
        book_obj = Book(name=name, author_id=author_id)
        db.add(book_obj)
        try:
            db.commit()
            message = save_book_msg
            status_code = 201
        except IntegrityError:
            db.rollback()
            message = save_book_failure_msg.format(name)
            status_code = 409
    else:
        message = author_not_exist
        status_code = 404

    return message, status_code


def get_books(db, author_id=None):
    """
    :param author_id:
    :param db:
    :return:
    """
    if author_id:
        books_data = [book.toDict() for book in db.query(Book).filter(Book.author_id == author_id).all()]
    else:
        books_data = [book.toDict() for book in db.query(Book).all()]
    return books_data


def get_book_by_id(db, id):
    """

    :param db:
    :param id:
    :return:
    """
    book_obj = db.query(Book).filter(Book.id == id).first()
    if book_obj:
        return book_obj.toDict(), 200
    else:
        return [], 404


def update_book_by_id(db, id, name, author_id):
    """

    :param author_id:
    :param db:
    :param id:
    :param name:
    :return:
    """
    """
    first check book exist against provided id
    """
    book_status = get_book_by_id(db=db, id=id)[1]
    if book_status == 200:
        db.query(Book).filter(Book.id == id).update({
            "name": name,
            "author_id": author_id
        })
        db.commit()
        return update_book_msg, 200
    else:
        return no_record_found, 404


def delete_book_by_id(db, id):
    """

    :param db:
    :param id:
    :return:
    """
    """
    first check book exist against provided id
    """
    book_status = get_book_by_id(db=db, id=id)[1]
    if book_status == 200:
        db.query(Book).filter(Book.id == id).delete()
        db.commit()
        return delete_book_msg, 200
    else:
        return no_record_found, 404