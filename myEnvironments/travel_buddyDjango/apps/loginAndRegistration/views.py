# from django.shortcuts import render, redirect, HttpResponse
# from django.contrib import messages
# from django.core.urlresolvers import reverse
# from .models import User
# import bcrypt
#
# def index(request):
#     print User.objects.all()
#     if not 'errors' in request.session:
#         request.session['errors']=[]
#     return render(request, 'loginAndRegistration/index.html')
#
# def register(request):
#     postData= {
#         "name":request.POST['name'],
#         "username": request.POST['username'],
#         "password": request.POST['password'],
#         "password_confirmation":request.POST['password_confirmation']
#     }
#     results= User.objects.UserValidator(postData)
#     if results[0]:
#         for err in results[1]:
#             messages.error(request,err)
#         return render (request, 'loginAndRegistration/index.html')
#     else:
#         request.session['user_id']= results[1].id
#         request.session['name']=results[1].name
#         return redirect(reverse('userTravel:index'))
#
#
# def login(request):
#     postData={
#         "username": request.POST['username'],
#         "password": request.POST['password']
#     }
#     results = User.objects.userLogin(postData)
#     if results == None:
#         messages.error(request, "wrong credentials")
#         return redirect(reverse('loginAndRegistration:index'))
#     elif results[0]:
#         request.session['name']= results[1].name
#         request.session['user_id']= results[1].id
#         return redirect(reverse("userTravel:index"))
#     else:
#         messages.error(request, results[1])
#         return redirect(reverse('loginAndRegistration:index'))
#
# # def success(request):
# #     context={
# #         'user': User.objects.get(id=request.session['loggedinuser'])
# #     }
# #     return render(request, 'userTravel/index.html', context)
#
# def delete(request, id):
#     if request.method=="GET":
#         User.objects.filter(id=id).delete()
#         return redirect(reverse('loginAndRegistration:index'))
#
# def logout(request):
#     request.session.pop('user_id')
#     return redirect(reverse("loginAndRegistration:index"))
