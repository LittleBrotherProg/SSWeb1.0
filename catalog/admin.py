from django.contrib import admin
from daterangefilter.filters import PastDateRangeFilter, FutureDateRangeFilter
# Register your models here.
from .models import Customer, Services, Servis_order



class Servis_orderInline(admin.TabularInline):
    model = Servis_order


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('First_name', 'Last_name', 'Phone_numb')
    fields = [('First_name', 'Last_name'), 'Phone_numb']
    inlines = [Servis_orderInline]


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    pass


@admin.register(Servis_order)
class Servis_orderAdmin(admin.ModelAdmin):
    search_fields = ("cust__First_name", "cust__Last_name")
    list_display = ('cust', 'status', 'created_at', 'publish_at', 'Services')
    list_filter = [
        ('created_at', PastDateRangeFilter),
        ('publish_at', FutureDateRangeFilter),
        ('status'),
        ('Services'),
    ]


    fields = ['id', ('cust',  'Services'), 'status']
