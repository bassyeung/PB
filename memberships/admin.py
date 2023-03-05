from django.contrib import admin

from memberships.models import Membership
# Register your models here.

class MembershipAdmin(admin.ModelAdmin):
    list_display = ('channel','title','level','price','pic','id')
    list_display_links=('channel','title','level','price','pic')
    search_fields = ('channel','title','level')
    list_per_page = 20

admin.site.register(Membership, MembershipAdmin )
