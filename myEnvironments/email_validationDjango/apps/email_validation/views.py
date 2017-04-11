from django.shortcuts import render, redirect, HttpResponse
from .models import Email

def index(request):
    return render(request, 'email_validation/index.html')

def process(request):
    results= Email.objects.emailValidator(request.POST['email'])
    if (results[0]):
        # request.session['currEmail']=request.POST['email']
        return redirect("/success")
    else:
        context={
            'error': results[1]
        }
        return render(request, 'email_validation/index.html', context)

def success(request):
    context = {
        'emails': Email.objects.all(),
        'currEmail': Email.objects.last()
    }
    if context['currEmail']:
        context['currEmail']= context['currEmail'].emailAddress

    return render(request, 'email_validation/success.html', context)
#
def delete(request, id):
    if Email.objects.filter(id=id).delete():
        return redirect('/success')
