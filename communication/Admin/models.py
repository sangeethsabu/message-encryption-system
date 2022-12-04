from django.db import models

# Create your models here.
class Login(models.Model):
    uname=models.CharField(max_length=50)
    pwd=models.BigIntegerField()
    utype=models.CharField(max_length=10)
class major(models.Model):
    mname=models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    bgrp = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.CharField(max_length=20)
    photo = models.FileField(max_length=20,upload_to='file')
    fname = models.CharField(max_length=20)
    regno = models.IntegerField()
    exp=models.IntegerField()
    uname = models.CharField(max_length=20)
    pwd=models.CharField(max_length=20)
class operation(models.Model):
    oname=models.CharField(max_length=20)
    details=models.CharField(max_length=250)
    odate=models.CharField(max_length=20)

    rname=models.CharField(max_length=20)
    rtotal=models.IntegerField()
    gname=models.CharField(max_length=20)
    gtotal=models.IntegerField()
    cname=models.CharField(max_length=20)
    ctotal=models.IntegerField()
    lname=models.CharField(max_length=20)
    ltotal=models.IntegerField()

