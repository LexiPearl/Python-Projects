from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Friendship(models.Model):
    friend1 = models.ForeignKey(User, models.DO_NOTHING, related_name="friend1")
    friend2 = models.ForeignKey(User, models.DO_NOTHING, related_name="friend2")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
