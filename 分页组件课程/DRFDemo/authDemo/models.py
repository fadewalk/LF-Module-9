from django.db import models

# Create your models here.


class User(models.Model):

    username = models.CharField(max_length=32)
    pwd = models.CharField(max_length=16)
    token = models.UUIDField()
    type = models.IntegerField(choices=((1, "vip"), (2, "vvip"), (3, "普通")), default=3)
