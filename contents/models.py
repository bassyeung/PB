# ===============================================
# filename......: /contents/model.py
# purpose.......: create model for contents
# date created..: 2023-2-14
# date modified.: 2023-2-15
# created by....: Jacky Chan
# ===============================================

from django.db import models
from datetime import date, datetime
from userdetails.models import Userdetail
from channels.models import Channel
#DATE_INPUT_FORMATS = ['%Y-%m-%d']
# pow = models.BooleanField(default=False)

class Content(models.Model):  
    channel     = models.ForeignKey(Channel, on_delete=models.DO_NOTHING)
    user        = models.ForeignKey(Userdetail, on_delete=models.DO_NOTHING)
    title       = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    level       = models.IntegerField()
    image       = models.ImageField(upload_to='images/')
    video       = models.FileField(upload_to='videos/', null=True, blank=True)
    videolink   = models.CharField(max_length=250, null=True, blank=True)
    youtubelink = models.CharField(max_length=250, null=True, blank=True)
    dateupload  = models.DateTimeField(default=datetime.now)
    tag         = models.CharField(max_length=250, null=True, blank=True)
 
    def __str__(self):
        return self.title



class Contentmedia(models.Model):  
    content     = models.ForeignKey(Content, on_delete=models.DO_NOTHING)
    channel     = models.ForeignKey(Channel, on_delete=models.DO_NOTHING)
    user        = models.ForeignKey(Userdetail, on_delete=models.DO_NOTHING)
    media_type  = models.CharField(max_length=1, null=True, blank=True) 
    media_name  = models.CharField(max_length=100, null=True, blank=True)
    media_path  = models.CharField(max_length=200, null=True, blank=True)
    media_image = models.ImageField(upload_to='images/')
 
    def __str__(self):
        return self.content.title