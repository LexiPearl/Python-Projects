from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from django.db.models import Count
from django.core.urlresolvers import reverse
from ..loginAndRegistration.models import User
from .models import Poke

def existingUser(request):
    return 'name' in request.session

def dashboard(request):
    if not existingUser(request):
        return redirect(reverse("loginAndRegistration:index"))
    currUser=Poke.objects.filter(user_id_id=request.session['user_id'])
    #all of the poke objects where the person being poked is the current user

    otherUser=User.objects.exclude(id=request.session['user_id'])
        #all the users excluding current user

    totalPokes=Poke.objects.filter(user_id_id=request.session['user_id']).annotate(num_pokes=Count('poker_id_id')).order_by('-num_pokes')
    #all of the poke information for the current user adding the total number of times they were the poker

    numPokes=User.objects.filter(poker_id__user_id=request.session['user_id']).annotate(num_pokes=Count('poker_id__user_id'))
    #all of the relationships between poker and pokee filtered where the user is the current user and adding the total number of pokes by each poker

    pokedYou=len(numPokes)

    context={
        "totalPokes": totalPokes,
        "currUser": currUser,
        "otherUser": otherUser,
        "pokedYou":pokedYou,
        "numPokes":numPokes
    }
    return render(request, "beltTwoApp/index.html", context)

def addPoke(request, pokee_id):
    if not existingUser(request):
        return redirect(reverse("loginAndRegistration:index"))
    postData={
        "poker_id":request.session['user_id'],
        "user_id": pokee_id,
    }
    print postData
    results=Poke.objects.add_poke(postData)
    context={
        "users":User.objects.all(),
        "pokes": Poke.objects.all()
    }
    return redirect(reverse('beltTwoApp:dashboard'))

def logout(request):
    if not existingUser(request):
        return redirect(reverse("loginAndRegistration:index"))
    request.session.pop('user_id')
    request.session.pop('name')
    request.session.pop('alias')
    return redirect(reverse("loginAndRegistration:index"))
