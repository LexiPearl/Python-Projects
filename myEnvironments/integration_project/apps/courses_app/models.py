from __future__ import unicode_literals
from django.db import models
from ..loginAndRegistration.models import User

class CourseManager(models.Manager):
    def add_to_user(self, postData):
        course=self.get(id=postData['course'])
        user=User.objects.get(id=postData['user'])
        print user.first_name
        print "*"*50
        print "*"*50

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
