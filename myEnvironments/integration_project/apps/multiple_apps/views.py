from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.db.models import Count
from ..courses_app.models import Course
from ..loginAndRegistration.models import User
from ..multiple_apps.models import User_Course


def index (request):
    users= User.objects.all()
    courses= Course.objects.all().annotate(usercount=Count('usercourse'))
    print users
    print "*"*50
    print courses
    context={
        'users': users,
        'courses':courses,
    }
    print context
    return render(request, "multiple_apps/index.html", context)

def create(request):
    add_to_course = User_Course.objects.create(user_id=request.POST['user'], course_id = request.POST['course'])
    add_to_course.save()
    return redirect(reverse('multiple_apps:index'))
