
from api.constants import save_author_msg, no_record_found, update_author_msg, delete_author_msg, save_book_msg
from api.book.models import Author, Book


def get_authors(db):
    """

    :param db:
    :return:
    """
    authors_data = [author.toDict() for author in db.query(Author).all()]
    return authors_data


def get_author_by_id(db, id):
    """

    :param db:
    :param id:
    :return:
    """
    author_obj = db.query(Author).filter(Author.id == id).first()
    if author_obj:
        return author_obj.toDict(), 200
    else:
        return [], 404


def save_author(db, name):
    """

    :param db:
    :param name:
    :return:
    """
    author_obj = Author(name=name)
    db.add(author_obj)
    db.commit()
    message = save_author_msg
    status_code = 201
    return message , status_code


def update_author_by_id(db, id, name):
    """

    :param db:
    :param id:
    :param name:
    :return:
    """
    """
    first check author exist against provided id
    """
    author_status = get_author_by_id(db=db, id=id)[1]
    if author_status == 200:
        db.query(Author).filter(Author.id == id).update({
            "name": name
        })
        db.commit()
        message = update_author_msg
        status_code = 200
    else:
        message = no_record_found
        status_code = 404
    return message, status_code


def delete_author_by_id(db, id):
    """

    :param db:
    :param id:
    :return:
    """
    """
    first check author exist against provided id
    """
    author_status = get_author_by_id(db=db, id=id)[1]
    if author_status == 200:
        author_obj = db.query(Author).filter(Author.id == id).first()
        db.delete(author_obj)
        """
        Delete All the references of this author id in book table
        """
        db.query(Book).filter(Book.author_id == id).delete()
        db.commit()
        message = delete_author_msg
        status_code = 200
    else:
        message = no_record_found
        status_code = 404
    return message, status_code

