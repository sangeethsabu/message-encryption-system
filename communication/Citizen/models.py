from django.db import models

# Create your models here.
class reg(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    hname=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    pin=models.IntegerField()
    lmark=models.CharField(max_length=20)
    photo=models.FileField(upload_to='file')
    cno=models.BigIntegerField()
    email=models.CharField(max_length=50)
    uname=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default='')
class complaint(models.Model):
    cid=models.IntegerField()
    complaint=models.CharField(max_length=50)
    desc=models.TextField()
    date=models.DateField()
    status=models.CharField(max_length=20)
class request1(models.Model):
    cid=models.IntegerField()
    rtype=models.CharField(max_length=50)
    details=models.TextField()
    date=models.DateField()
    status=models.CharField(max_length=20)
