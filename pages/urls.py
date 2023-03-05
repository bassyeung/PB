from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('support', views.support, name='support'),
    path('otherservices', views.otherservices, name='otherservices'),    
    #path('creators', views.creators, name='creators'), 
    path('creatorbox', views.creatorbox, name='creatorbox')
]