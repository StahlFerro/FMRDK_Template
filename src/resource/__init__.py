from flask_restful import Api
from src.resource.book import BookAPI, BookListAPI


api = Api(prefix="/api/v1")
api.add_resource(BookListAPI, '/books')
api.add_resource(BookAPI, '/books/<int:id>')

