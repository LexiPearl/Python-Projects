from django.shortcuts import render, redirect
from .models import Course
from ..multiple_apps.models import User_Course
from django.urls import reverse

def index(request):
    context = {
        'courses': Course.objects.all()
        }
    return render(request, 'courses_app/index.html', context)

def process(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect(reverse("courses_app:index"))

def remove(request, id):
	context = {
	'courses': Course.objects.filter(id=id)
	}
	return render(request, "courses/delete.html", context)

def delete(request, id):
    delete = Course.objects.get(id=id)
    if 'yeabye' in request.POST:
        Course.objects.filter(id=id).delete()
        User_Course.objects.filter(course_id=id).delete()
        return redirect (reverse("courses_app:index"))
    else:
        return redirect(reverse("courses_app:index"))

def logout(request):
	request.session.pop('user_id')
	request.session.pop('name')
	return redirect('/')
