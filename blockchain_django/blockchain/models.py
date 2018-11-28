# coding:utf-8

from django.db import models

# Create your models here.
class Block(models.Model):
    index = models.IntegerField()
    timestamp = models.TimeField()
    #数据字段部分
    trackNum = models.CharField(max_length = 64)#运单号
    deviceId = models.CharField(max_length = 64)
    deviceName = models.CharField(max_length = 64)
    dpCreationTime = models.TimeField()
    location = models.CharField(max_length = 64)
    image = models.CharField(max_length = 64)#图片文件名
    
    previous_hash = models.CharField(max_length = 64)
    self_hash = models.CharField(max_length = 64)

class User(models.Model):
    uid = models.CharField(max_length = 13)#身份证号
    trackNumSet = models.TextField()
    name = models.CharField(max_length = 32)
