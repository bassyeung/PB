from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from contents import views


urlpatterns = [
    path('',include('pages.urls')),
    path('userdetails/', include('userdetails.urls')),
    path('channels/', include('channels.urls')),
    path('contents/', include('contents.urls')),
    #path('search', include('contents.urls')),
    #path('searchb', include('contents.urls')),
    #path('contentlist', include('contents.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
