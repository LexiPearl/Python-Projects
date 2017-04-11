from __future__ import unicode_literals
from django.db import models
import bcrypt

import re

EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
FIRSTNAME_REGEX = re.compile(r'^[a-zA-Z]*$')
LASTNAME_REGEX = re.compile(r'^[a-zA-Z]*$')

class UserManager(models.Manager):
    def UserValidator(self, postData):
        flag=False
        errors=[]
        if len(postData['email']) <2:
            flag=True
            errors.append("Email cannot be empty!")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("Invalid email.")
            flag=True
        if len(postData['first_name']) < 2:
            errors.append("First name cannot be empty!")
            flag=True
        elif not FIRSTNAME_REGEX.match(postData['first_name']):
            errors.append("Invalid first name!")
            flat=True
        if len(postData['last_name']) < 2:
            flag=True
            errors.append("Last name cannot be empty!")
        elif not LASTNAME_REGEX.match(postData['last_name']):
            flag=True
            errors.append ("Invalid last name!")
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
                first_name=postData['first_name'],
                last_name=postData['last_name'],
                email=postData['email'],
                password=pwhash)
            user = User.objects.last()
            return (flag, user)
        return (flag, errors)
    def userLogin(self, postData):
        user= User.objects.get(email=postData['email'])
        password= postData['password'].encode()
        hashed=user.password.encode()
        if bcrypt.hashpw(password, hashed )== hashed and user:
            return (True, user)
        else:
            return (False, "Email and password do not match")

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= UserManager()
