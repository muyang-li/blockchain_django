# coding:utf-8

from django.db import models

# Create your models here.
class Block(models.Model):
    index = models.IntegerField()
    timestamp = models.DateTimeField(verbose_name=u"区块时间戳",default=None)
    #数据字段部分
    trackNum = models.CharField(max_length = 64,default='0')#运单号
    deviceId = models.CharField(max_length = 64,default='0')#安检机id
    deviceName = models.CharField(max_length = 64,default='0')#安检机名字
    dpCreationTime = models.DateTimeField(verbose_name=u"过包时间戳",default=None)#过包时间
    location = models.CharField(max_length = 64,default='0')#安检机地点
    image = models.CharField(max_length = 64,default='0')#图片文件名

    previous_hash = models.CharField(max_length = 64,default='0')
    self_hash = models.CharField(max_length = 64,default='0')

class CommonUser(models.Model):
    uid = models.CharField(max_length = 13,default='0')#身份证号
    trackNumSet = models.TextField(default='0')#运单号集合，用逗号隔开
    name = models.CharField(max_length = 32,default='0')
