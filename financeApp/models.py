from django.db import models

# Create your models here.

class userinfo(models.Model):
    name = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)



        