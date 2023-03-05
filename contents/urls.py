from django.contrib import admin
from django.urls import path
from contents import views

#from django.conf.urls import include, url
from django.conf import settings  
from django.conf.urls.static import static  
from django.contrib.auth import views as auth_views
#from users import views as user_views


urlpatterns = [
    path('', views.search_view, name='search'),
    path('search', views.search_view, name='search'),
    path('contentlist', views.contentlist_view, name='contentlist'),
    path('contentins', views.content_insert_view, name='contentins'), 
    path('contentinsertb', views.content_insertb_view, name='contentinsertb'),     
    path('<int:content_id>', views.content, name='content'),
    path('contentupdate/<int:id>', views.content_update_view, name='contentupdate'),   
]


#if settings.DEBUG:
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

