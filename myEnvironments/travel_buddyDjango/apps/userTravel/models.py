# from __future__ import unicode_literals
# from django.db import models
# from ..loginAndRegistration.models import User
# from ..travelPlans.models import Destination

#
# class User_Travel_Manager(models.Manager):
# 	def add_user_to_travel(self):
# 			return (True, "true")

# class User_Travel(models.Model):
# 	joined_traveller= models.ForeignKey(User, related_name="traveluser")
# 	joined_destination = models.ForeignKey(Destination, related_name="usertravel")
# 	created_at = models.DateTimeField(auto_now_add = True)
# 	updated_at = models.DateTimeField(auto_now = True)
# 	objects = User_Travel_Manager()
