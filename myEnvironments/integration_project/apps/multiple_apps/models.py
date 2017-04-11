from __future__ import unicode_literals
from django.db import models
from ..loginAndRegistration.models import User
from ..courses_app.models import Course

class User_Course_Manager(models.Manager):
	def add_to_course(self):
        	return (True, "true")

class User_Course(models.Model):
	user = models.ForeignKey(User, related_name="courseuser")
	course = models.ForeignKey(Course, related_name="usercourse")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = User_Course_Manager()
