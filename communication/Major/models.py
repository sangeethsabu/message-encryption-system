from django.db import models

# Create your models here.
class officer(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    bgrp=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    phone=models.IntegerField()
    email=models.CharField(max_length=20)
    dname=models.CharField(max_length=20)
    photo=models.FileField(max_length=20,upload_to='file')
    fname=models.CharField(max_length=20)
    regno=models.IntegerField()
    uname=models.CharField(max_length=20)
class team(models.Model):
    tcode=models.CharField(max_length=20)
    offid=models.IntegerField()
    mid=models.IntegerField()
    oid=models.IntegerField()
class majortextmsg(models.Model):
    mid=models.IntegerField()
    oid=models.IntegerField()
    msg=models.TextField()
    encmsg=models.TextField(default='')
    private = models.CharField(max_length=50)
    public = models.CharField(max_length=50)

