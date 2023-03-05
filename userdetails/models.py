from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Userdetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    creator_status = models.BooleanField(default=False)
    credit_card = models.CharField(blank = True,max_length=100)
    bank_account = models.CharField(blank = True, max_length=100)
    address = models.CharField(blank = True,max_length=200)
    country = models.CharField(blank = True,max_length=100)
    phone_num = models.CharField(blank = True,max_length=30)
    facebook_ac = models.CharField(blank = True,max_length=30)
    ig_ac = models.CharField(blank = True,max_length=200)
    linkedin_ac = models.CharField(blank = True,max_length=200)
    patreon_ac = models.CharField(blank = True,max_length=200)
    pinterest_ac = models.CharField(blank = True,max_length=200)
    youtube_ac = models.CharField(blank = True,max_length=200)
    twitter_ac = models.CharField(blank = True,max_length=200)   
    user_icon = models.ImageField(upload_to='photos/users/%Y/%m/%d', blank=True)
    start_date = models.DateTimeField(default=datetime.now)
    status = models.CharField(
        choices=[('active','active'),('banned','banned')],
        max_length=200)
    
    
    def __str__(self):
        return self.user.username




