# coding:utf-8

from django.db import models

# Create your models here.
class Block(models.Model):
    index = models.IntegerField()
    timestamp = models.TimeField()
    data = models.TextField()
    previous_hash = models.CharField(max_length = 64)
    self_hash = models.CharField(max_length = 64)