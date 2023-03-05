from django.contrib import admin

from subscriptions.models import Subscription
 

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user','channel','level','start_date','payment_date','end_date','id')
    list_display_links=('user','channel','level','start_date','payment_date','end_date')
    search_fields = ('channel','level')
    list_per_page = 20

admin.site.register(Subscription, SubscriptionAdmin )
