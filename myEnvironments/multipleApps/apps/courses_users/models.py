from __future__ import unicode_literals
from django.db import models
from ..loginregistration.models import User
from ..courses.models import Course

class User_Course_Manager(models.Manager):
	def add_user_to_course(self):
			return (True, "true")

# Create your models here.
class User_Course(models.Model):
	user = models.ForeignKey(User, related_name="courseuser")
	course = models.ForeignKey(Course, related_name="usercourse")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	user_course_Mgr = User_Course_Manager()
