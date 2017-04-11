from __future__ import unicode_literals

from django.db import models

import re

email_regex=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



# Create your models here.


class emailManager(models.Manager):
    def emailValidator(self, email):
        if email_regex.match(email):
            Email.objects.create(emailAddress = email)
            return (True, "Email was valid and added to database.")
        else:
            return (False, "Invalid email.")
        print email

class Email(models.Model):
    emailAddress = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= emailManager()
