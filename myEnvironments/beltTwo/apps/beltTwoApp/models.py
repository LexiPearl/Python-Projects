from __future__ import unicode_literals
from django.db import models
from ..loginAndRegistration.models import User

class NewPokeManager(models.Manager):
    def add_poke(self, postData):
        addPoke=Poke.objects.create(user_id_id=postData['user_id'], poker_id_id=postData['poker_id'])
        return(addPoke)

class Poke(models.Model):
    user_id=models.ForeignKey(User, related_name="user_id")
    poker_id=models.ForeignKey(User, related_name="poker_id")
    created_at=models.DateTimeField(auto_now_add =True)
    updated_at=models.DateTimeField(auto_now =True)
    objects=NewPokeManager()
