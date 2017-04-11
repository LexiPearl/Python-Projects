from django.shortcuts import render, HttpResponse, redirect
from .models import Course
from ..courses_users.models import User_Course

# Create your views here.
def index(request):
	context = {
	'courses': Course.courseMgr.all()
	}
	return render(request, "courses/index.html", context)

def add(request):
	Course.courseMgr.create(name= request.POST['name'],description=request.POST['description'])
	
	return redirect('/courses')

def course(request, id):
	context = {
	'courses': Course.courseMgr.filter(id=id)
	}
	return render(request, "courses/delete.html", context)

def delete(request, id):
	delete = Course.courseMgr.get(id=id)
	Course.courseMgr.filter(id=id).delete()
	User_Course.user_course_Mgr.filter(course_id=id).delete()
	return redirect('/courses')

def logout(request):
	request.session.pop('user_id')
	request.session.pop('name')
	return redirect('/')
