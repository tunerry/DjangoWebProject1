"""
Definition of models.
"""

from django.db import models

# Create your models here.
class user(models.Model):
    userID = models.CharField('ID', max_length=20,primary_key=True)
    userName = models.CharField('用户名', max_length=150)
    gender = models.CharField('性别', max_length=2,default='保密')