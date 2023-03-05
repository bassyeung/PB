from django.contrib import admin

from channels.models import Channel
# Register your models here.

class ChannelAdmin(admin.ModelAdmin):
    list_display = ('user','title','link','start_date','icon','banner','video','status','tag','id')
    list_display_links=('user','title','link','start_date','status')
    search_fields = ('user','title')
    list_per_page = 20

admin.site.register(Channel, ChannelAdmin )
