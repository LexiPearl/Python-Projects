from django.shortcuts import render, HttpResponse, redirect
import datetime
import random


def index(request):
    # session.clear()
    if request.method == 'GET':
        if 'gold' not in request.session:
            request.session['gold'] = 0
            request.session['info']=[]
    return render(request, "ninja_gold/index.html")

def process(request):
    if request.method == "POST":
        time= datetime.datetime.now()
        if request.POST['action'] == 'farm':
            randomgold= random.randrange(10,21)
            location='farm'
        if request.POST['action'] == 'cave':
            randomgold= random.randrange(5,11)
            location='cave'
        if request.POST['action'] == 'house':
            randomgold= random.randrange(2,6)
            location='house'
        if request.POST['action'] == 'casino':
            randomgold= random.randrange(-50,51)
            location='casino'
        if randomgold > -1:
            sentence= ("Earned " + str(randomgold) + " from the " + location+"! "+ str(time))
            color= 'green'
            request.session['info'].insert(0,{'sentence': sentence, 'class': color})
        if randomgold < 0:
            sentence= ("Entered a casino and lost "+ str(randomgold) + " golds...Ouch. "+ str(time))
            color= 'red'
            request.session['info'].insert(0,{'sentence': sentence, 'class': color})
        request.session['gold'] += randomgold
        return redirect("/")

def clear(request):
        if request.method == "GET":
            request.session.flush()
        return redirect("/")
