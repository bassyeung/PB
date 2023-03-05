from django.contrib import admin
from userdetails.models import Userdetail
# Register your models here.

class UserdetailAdmin(admin.ModelAdmin):
    list_display = ('user','creator_status','user_icon','credit_card','country','phone_num','start_date','status','id')
    list_display_links=('user','country')
    search_fields = ('user','country')
    list_per_page = 25

admin.site.register(Userdetail, UserdetailAdmin)