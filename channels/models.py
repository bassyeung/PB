from django.db import models
from datetime import datetime
from userdetails.models import Userdetail
from django.contrib.auth.models import User
# Create your models here.


class Channel(models.Model):
    #owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(Userdetail, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    link = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(default=datetime.now, blank=True)
    icon = models.ImageField(upload_to='photos/channels/%Y/%m/%d', blank=True)
    banner = models.ImageField(upload_to='photos/channels/%Y/%m/%d', blank=True)
    video = models.CharField(max_length=200)
    category = models.CharField(choices=[('IT','IT'),('music','music'),('games','games'),('finance','finance'),('style','style'),('fashion','fashion'),('food','food')],max_length=200)
    status = models.CharField(max_length=1)
    tag = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title


