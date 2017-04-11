from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

def index(request):
    if 'name' not in request.session:
        request.session['name']=""
    if 'comment' not in request.session:
        request.session['comment']=""
    return render(request, "survey_form/index.html")

def process(request):
    if request.method == "POST":
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['name'] = request.POST['name']
        request.session['comment'] = request.POST['comment']
        return render (request, "survey_form/result.html")
    else:
        return redirect(reverse('survey_form:survey_form_index'))

def result(request):
    if request.method == "POST":
        return render(request, "survey_form/result.html")
    else:
        return redirect(reverse('survey_form:survey_form_index'))

def goback(request):
    if request.method == "POST":
        del request.session['name']
        del request.session['comment']
        del request.session['language']
        del request.session['location']
        return redirect(reverse("survey_form:survey_form_index"))
