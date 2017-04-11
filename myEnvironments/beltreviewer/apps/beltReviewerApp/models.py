from __future__ import unicode_literals
from django.db import models
from ..loginAndRegistration.models import User

class BookManager(models.Manager):
    def add_book(self, postData):
        flag=False
        errors=[]
        if len(postData['title'])<1:
            flag=True
            errors.append("Destination cannot be empty!")
        if len(postData['author1']) and len(postData['author2'])<0:
            flag=True
            errors.append("You can have to have an author!")
        if len(postData['author1']) and len(postData['author2'])>1:
            flag=True
            errors.append("You can only have one author!")
        if postData['review'] < 1:
            flag=True
            errors.append("Review cannot be empty!")
        if postData['rating']< 1:
            flag=True
            errors.append("Rating has to be between 1 & 5!")
        if not flag:
            addBook= Book.objects.create(title=postData['title'])
            return (flag, addBook)
        return (flag, errors)
class AuthorManager(models.Manager):
    def add_author(self, postData, book_id):
        flag=False
        if len(postData['author1'])>1:
            author=postData['author1']
        else:
            author=postData['author2']
            name=Author.objects.all()
            for x in name:
                if author==x.author:
                    id=x.id
                    addAuthor= Author.objects.create(id=id, book_id=book_id)
                    return (flag, addAuthor)
            addAuthor= Author.objects.create(author=author, book_id=book_id)
            return (flag, addAuthor)

class BookReviewManager(models.Manager):
    def add_review_to_book(self,postData, book_id):
        flag=False
        errors=[]
        if postData['review']<1:
            flag=True
            errors.append("Review cannot be empty!")
        if postData['rating']<1:
            flag=True
            errors.append("Rating has to be between 1 & 5!")
        if not flag:
            addBookReview= BookReview.objects.create(rating=postData['rating'], review=postData['review'], book_reviewer_id=postData['user'], book_title_id=book_id)
            return (flag, addBookReview)
        return (flag, errors)

class Book(models.Model):
    title = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= BookManager()

class Author(models.Model):
    book=models.ForeignKey('Book')
    author=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=AuthorManager()

class BookReview(models.Model):
    rating=models.IntegerField()
    review=models.TextField()
    book_reviewer= models.ForeignKey(User, related_name="book_reviewer")
    book_title = models.ForeignKey(Book, related_name="book_title")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=BookReviewManager()
