from django.db import models

# Create your models here.
class officertextmsg(models.Model):
    mid=models.IntegerField()
    oid=models.IntegerField()
    msg=models.TextField()
    encmsg=models.TextField(default='')
    private = models.CharField(max_length=50)
    public = models.CharField(max_length=50)
