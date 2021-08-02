from mongoengine import Document, ListField, StringField, ObjectIdField, DateTimeField


class Book(Document):
    title = StringField(required=True, max_length=240)
    author = StringField(required=True, max_length=120)
    isbn = StringField(required=False, max_length=13)
    published_date = DateTimeField(required=True)
