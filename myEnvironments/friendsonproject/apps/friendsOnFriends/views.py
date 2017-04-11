from django.shortcuts import render, redirect
from .models import User, Friendship

# Create your views here.
def index(request):
    friendships = Friendship.objects.all()
    friends = User.objects.all()
    context = {
        'friends': friends,
        'friendships': friendships
        }
    return render(request, 'friendsOnFriends/index.html', context)

def add_friend(request):
    User.objects.create(name=request.POST['friend'])
    friendships = Friendship.objects.all()
    friends = User.objects.all()
    context = {
        'friends': friends,
        'friendships': friendships
        }
    print "*"*50
    print 'friend added'
    return render(request, 'friendsOnFriends/index.html', context)

    # return redirect(request, '/', context)

def add_friendship(request):
    friend1 = User.objects.get(id=request.POST['friend1'])
    friend2 = User.objects.get(id=request.POST['friend2'])
    Friendship.objects.create(friend1=friend1, friend2=friend2)
    friendships = Friendship.objects.all()
    friends = User.objects.all()
    context = {
        'friends': friends,
        'friendships': friendships
        }
    return render(request, 'friendsOnFriends/index.html', context)

    # return redirect(request, '/', context)
