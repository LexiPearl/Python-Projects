from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

NAME_REGEX = re.compile(r'^[a-zA-Z]*$')

class UserManager(models.Manager):
    def UserValidator(self, postData):
        flag=False
        errors=[]
        if len(postData['name']) < 3:
            errors.append("Name must be at least 3 characters!")
            flag=True
        elif not NAME_REGEX.match(postData['name']):
            errors.append("Invalid name!")
            flag=True
        if len(postData['username']) <3:
            flag=True
            errors.append("Username must be at least 3 characters!")
        if len(postData['password'])<8:
            flag=True
            errors.append("Password length is invalid")
        if len(postData['password_confirmation']) < 1:
            errors.append("Confirm password cannot be empty!")
            flag=True
        if postData['password_confirmation'] != postData['password']:
            flag=True
            errors.append("Passwords do not match!")
        if not flag:
            pwhash= bcrypt.hashpw(postData['password'].encode(),bcrypt.gensalt())
            User.objects.create(
                name=postData['name'],
                username=postData['username'],
                password= pwhash )
            user = User.objects.last()
            return (flag, user)
        return (flag, errors)
    def userLogin(self, postData):
        login= User.objects.filter(username=postData['username'])
        if len(login)<1:
            return (False, "User does not exist in database")
        else:
            user= User.objects.get(username=postData['username'])
            password= postData['password'].encode()
            hashed=user.password.encode()
            if bcrypt.hashpw(password, hashed )== hashed and user:
                return (True, user)
            else:
                return (False, "Username and password do not match")

class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= UserManager()

class DestinationManager(models.Manager):
    def add_user_to_trip(self,postData):
        flag=False
        errors=[]
        if len(postData['destination'])<1:
            flag=True
            errors.append("Destination cannot be empty!")
        if len(postData['description'])<1:
            flag=True
            errors.append("Description cannot be empty!")
        if len(postData['datefrom'])<1:
            flag=True
            errors.append("Travel Date To cannot be empty")
        if len(postData['dateto'])<1:
            flag=True
            errors.append("Travel Date From cannot be empty")
        if not flag:
            destination= Destination.objects.create(destination=postData['destination'], description=postData['description'], datefrom=postData['datefrom'], dateto= postData['dateto'], destination_traveller=User.objects.get(id=postData['destination_traveller']))
            User_Travel.objects.create(joined_destination=postData['destination'], joined_traveller=postData['destination_traveller'])

            return (flag, destination)
        return (flag, errors)

class Destination(models.Model):
    destination_traveller= models.ForeignKey(User, related_name="traveller")
    destination = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    datefrom= models.DateTimeField(max_length=20)
    dateto= models.DateTimeField(max_length=20 )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= DestinationManager()
#
# class User_Travel_Manager(models.Manager):
# 	def add_user_to_travel(self):
# 			return (True, "true")

class User_Travel(models.Model):
	joined_traveller= models.ForeignKey(User, related_name="traveluser")
	joined_destination = models.ForeignKey(Destination, related_name="usertravel")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	# objects = User_Travel_Manager()
