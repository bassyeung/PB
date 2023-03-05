# ===============================================
# filename......: /contents/admin.py 
# purpose.......: show entry in admin page 
# date created..: 2023-2-14
# date modified.: 2023-2-15
# created by....: Jacky Chan
# ===============================================

from django.contrib import admin

from contents.models import Content, Contentmedia


class ContentAdmin(admin.ModelAdmin):
    list_display = ('channel','user','title','image','youtubelink','dateupload','tag','id')
    list_display_links=('channel','user','title','image','dateupload','tag')
    search_fields = ('title','tag')
    list_per_page = 20

admin.site.register(Content, ContentAdmin )



class ContentmediaAdmin(admin.ModelAdmin):
    list_display = ('channel','media_name','media_image','user','id')
    list_display_links=('channel','media_name','media_image','user')
    search_fields = ()
    list_per_page = 20

admin.site.register(Contentmedia, ContentmediaAdmin )


