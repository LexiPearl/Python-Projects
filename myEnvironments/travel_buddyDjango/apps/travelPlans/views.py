from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.urls import reverse
from .models import User, Destination, User_Travel
import bcrypt

def index(request):
    if not 'errors' in request.session:
        request.session['errors']=[]
    return render(request, 'travelPlans/index.html')

def register(request):
    postData= {
        "name":request.POST['name'],
        "username": request.POST['username'],
        "password": request.POST['password'],
        "password_confirmation":request.POST['password_confirmation']
    }
    results= User.objects.UserValidator(postData)
    if results[0]:
        for err in results[1]:
            messages.error(request,err)
        return render (request, 'travelPlans/index.html')
    else:
        request.session['user_id']= results[1].id
        request.session['name']=results[1].name
        return redirect(reverse('travelPlans:dashboard'))

def login(request):
    postData={
        "username": request.POST['username'],
        "password": request.POST['password']
    }
    results = User.objects.userLogin(postData)
    if results == None:
        messages.error(request, "wrong credentials")
        return redirect(reverse('travelPlans:index'))
    elif results[0]:
        request.session['name']= results[1].name
        request.session['user_id']= results[1].id
        return redirect(reverse("travelPlans:dashboard"))
    else:
        messages.error(request, results[1])
        return redirect(reverse('travelPlans:dashboard'))

def dashboard(request):
    # destination_traveller= User_Travel.objects.filter (id=request.session['user_id'])
    # joined_destination=User_Travel.objects.filter(id=id)
    user=User.objects.all(),
    destination=Destination.objects.all(),
    context={
        # "destination_traveller":destination_traveller,
        # "joined_destination": joined_destination,
        "user":user,
        "destination":destination
    }
    # print destination_traveller
    # print joined_destination
    print "*"* 50
    return render(request, 'travelPlans/usertravel.html', context)

def addTrip(request):
    if request.method=="GET":
        return render(request, 'travelPlans/addTrip.html')
    else:
        postData={
            "destination": request.POST['destination'],
            "description": request.POST['description'],
            "datefrom": request.POST['datefrom'],
            "dateto": request.POST['dateto'],
            "destination_traveller": request.session['user_id'],
            # "owner":request.session['owner']
        }
        results=Destination.objects.add_user_to_trip(postData)
        if results[0]:
            for err in results[1]:
                messages.error(request,err)
            return render(request, 'travelPlans/addTrip.html')
        return redirect(reverse('travelPlans:dashboard'))

def destination(request, id):
    context={
        'destination':Destination.objects.filter(id=id)
    }
    return render(request, 'travelPlans/destination.html', context)

def join(request, user_id, destination_id):
    joined_destination= User_Travel.objects.filter(joined_destination_id=destination_id)
    joined_traveller=User_Travel.objects.create (joined_traveller_id=user_id, joined_destination_id=destination_id)
    # print joined_destination
    # print joined_traveller
    return redirect(reverse( 'travelPlans:dashboard'))

def delete(request, id):
    Destination.objects.filter(id=id).delete()
    User_travel.objects.filter(destination_id=id).delete
    return redirect(reverse('travelPlans:dashboard'))

def logout(request):
    request.session.pop('user_id')
    request.session.pop('name')
    return redirect(reverse("travelPlans:index"))
