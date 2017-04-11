from django.shortcuts import render, redirect
from .models import Course

def index(request):
    context = {
        'courses': Course.objects.all()
        }
    return render(request, 'courses_app/index.html', context)

def process(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect("/")

def remove(request, id):
    context={
        'ids': Course.objects.filter(id=id),
    }
    return render(request, 'courses_app/delete.html',context)

#
def delete(request, id):
    if 'yeabye' in request.POST:
        Course.objects.filter(id=id).delete()
        return redirect ('/')
    else:
        return redirect('/')
