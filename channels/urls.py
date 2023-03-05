from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.channels, name='channels'),
    path('<int:id>/<slug:link>', views.channel, name='channel'),
    path('', include('contents.urls')),
    # path('index2', views.index2, name='index2'),
    path('subscription', views.subscription, name='subscription'),
    # path('memberships', views.memberships, name='memberships'),
    path('channelins', views.channel_insert_view, name='channelinsert'), 
    path('searchchannelcontent', views.search_channel_content_view, name='searchchannelcontent'),
]
