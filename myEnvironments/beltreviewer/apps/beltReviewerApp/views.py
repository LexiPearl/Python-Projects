from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from datetime import datetime
from django.core.urlresolvers import reverse
from ..loginAndRegistration.models import User
from .models import Book, Author, BookReview

def existingUser(request):
    return 'name' in request.session

def dashboard(request):
    if not existingUser(request):
        return redirect(reverse("loginAndRegistration:index"))
    recent= BookReview.objects.all().order_by('-created_at')[:3]
    allReviews=BookReview.objects.all().order_by('-created_at')[3:]
    context={
        "recents": recent,
        "allReviews": allReviews
    }
    return render(request, "beltReviewer/index.html",context)

def addBookReview(request):
    if not existingUser(request):
        return redirect(reverse("loginAndRegistration:index"))
    if request.method=="GET":
        context={
            "authors": Author.objects.all()
        }
        return render(request, 'beltReviewer/addBook.html', context)
    if request.method=="POST":
        postData={
            "user":request.session['user_id'],
            "author1": request.POST['author1'],
            "author2":request.POST['author2'],
            "title": request.POST['title'],
            "review":request.POST['review'],
            "rating": request.POST['rating'],
        }
        print postData
        results=Book.objects.add_book(postData)
        if results[0]:
            for err in results[1]:
                messages.error(request,err)
            return render(request, 'beltReviewer/addBook.html')
        else:
            book=Book.objects.last()
            book_id=book.id
            context={
                "book_id": book_id,
                "book": book
            }
            results2=Author.objects.add_author(postData, book_id)
            user_id=request.session['user_id']
            results3=BookReview.objects.add_review_to_book(postData, book_id)
            return render(request, 'beltReviewer/details.html', context)

def addReview(request, book_id):
    if not existingUser(request):
        return redirect(reverse("loginAndRegistration:index"))
    postData={
        "user":request.session['user_id'],
        "book_id": book_id,
        "review":request.POST['review'],
        "rating": request.POST['rating'],
    }
    results=BookReview.objects.add_review_to_book(postData, book_id)
    if results[0]:
        for err in results[1]:
            messages.error(request,err)

def bookInfo(request, book_id):
    if not existingUser(request):
        return redirect(reverse("loginAndRegistration:index"))
    if request.method=="GET":
        reviews=BookReview.objects.filter(book_title_id=book_id)
        context={
            "book": Book.objects.get(id=book_id),
            "reviews": reviews
            }
        return render(request, "beltReviewer/details.html", context)

def userInfo(request, id):
    if not existingUser(request):
        return redirect(reverse("loginAndRegistration:index"))
    user=User.objects.get(id=id)
    reviewer=BookReview.objects.filter(book_reviewer_id=id)
    # BookReview.objects.all().annotate(book_reviewer=.Count("id"))
    context={
        "user":user,
        "reviewer":reviewer
    }
    return render(request, 'beltReviewer/userinfo.html', context)

def delete(request, id):
    if not existingUser(request):
        return redirect(reverse("loginAndRegistration:index"))
    if BookReview.objects.get(id=id).delete():
        return redirect(reverse('beltReviewerApp:bookInfo'))

def logout(request):
    if not existingUser(request):
        return redirect(reverse("loginAndRegistration:index"))
    request.session.pop('user_id')
    request.session.pop('name')
    request.session.pop('alias')
    return redirect(reverse("loginAndRegistration:index"))
