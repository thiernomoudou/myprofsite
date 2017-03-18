from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=2000)

    def __str__(self):
        return '{}'.format(self.name)
