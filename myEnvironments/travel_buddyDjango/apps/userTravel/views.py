# from django.shortcuts import render, redirect
# from django.urls import reverse
# from ..travelPlans.models import Destination
# from ..loginAndRegistration.models import User
#
# def index(request):
#     context = {
#         'users' : User.objects.all(),
#         'destinations' : Destination.objects.all(),
#         # 'combined': User_Travel.objects.all(),
#         # 'alltrips': User_Travel.objects.exclude(id=request.session['user_id'])
#     }
#
#     print context
#     return render(request, 'userTravel/index.html', context)
#
# def add(request):
#     add_user_to_travel= User_Travel.objects.create(user_id=request.POST['user'], destination_id=request.POST['destination'])
#     add_user_to_trip.save()
#     return redirect(reverse('userTravel:index'))
#
# def logout(request):
#     request.session.pop('user_id')
#     request.session.pop('name')
#     return redirect(reverse('loginAndRegistration:index'))
#
# def join(request, user_id, destination_id):
#     user= request.session['user_id']
#     destination= destination_id
#     User_Travel.objects.create(user_id=user, destination_id=destination)
#     return redirect(reverse( 'userTravel:index'))
