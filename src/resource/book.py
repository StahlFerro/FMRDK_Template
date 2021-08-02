from flask import Response
from flask_restful import Resource, request
from src.models.book import Book


class BookListAPI(Resource):

    def get(self):
        books = Book.objects().to_json()
        return Response(books, mimetype="application/json", status=200)

    def post(self):
        req_json = request.json
        if type(req_json) is list:
            books_to_save = []
            for rq in req_json:
                book = Book(**rq)
                book.validate(clean=True)
                books_to_save.append(book)
                # print(book.pk)
            for valid_book in books_to_save:
                valid_book.save()
        else:
            book = Book(**req_json)
            book.save(validate=True, clean=True)
            # book.save(validate=True, clean=True)
            # print(book.pk)
        return Response(mimetype="application/json", status=201)


class BookAPI(Resource):

    def get(self, id):
        books = Book.objects().to_json()
        return Response(books, mimetype="application/json", status=200)
