from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import User
import bcrypt

def index(request):
    print User.objects.all()
    if not 'errors' in request.session:
        request.session['errors']=[]
    return render(request, 'loginAndRegistration/index.html')



def process(request):
    postData= {
        "first_name":request.POST['first_name'],
        "last_name": request.POST['last_name'],
        "email": request.POST['email'],
        "password": request.POST['password'],
        "password_confirmation":request.POST['password_confirmation']
    }
    results= User.objects.UserValidator(postData)
    if results[0]:
        for err in results[1]:
            messages.error(request,err)
        return render (request, 'loginAndRegistration/index.html')
    else:
        request.session['loggedinuser']= results[1].id
        # return redirect( '/success')
        return redirect(reverse('success'))


def login(request):
    postData={
        "email": request.POST['email'],
        "password": request.POST['password']
    }
    results = User.objects.userLogin(postData)
    if results == None:
        messages.error(request, "wrong credentials")
        return redirect('/')
    elif results[0]:
        request.session['loggedinuser']= results[1].id
        return redirect(reverse("success"))
    else:
        messages.error(request, results[1])
        return redirect('/')

def success(request):
    context={
        'user': User.objects.get(id=request.session['loggedinuser'])
    }
    return render(request, 'loginAndRegistration/success.html', context)

def delete(request, id):
    if User.objects.filter(id=id).delete():
        return redirect('/')

def logout(request):
    request.session.pop('loggedinuser')
    return redirect("/")
