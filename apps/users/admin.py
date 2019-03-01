from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from .models import Watchman, Resident

@admin.register(Watchman)
class WatchmanAdmin(admin.ModelAdmin):
    """ Watchman Admin """
    list_display = (
        'pk',
        'id_num',
    )


@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    """ Resident Admin """
    list_display = (
        'pk',
        'building_num',
        'apartment_num',
        'parking_lot_num',
        'property_relation'
    )
