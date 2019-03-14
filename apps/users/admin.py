from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from .models import User, WatchmanProfile, ResidentProfile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """ User Admin """
    list_display = (
        'pk',
        'username',
        'phone_number',
        'email',
        'user_role'
    )


@admin.register(WatchmanProfile)
class WatchmanAdmin(admin.ModelAdmin):
    """ Watchman Admin """
    list_display = (
        'pk',
        'user',
        'id_num',
    )


@admin.register(ResidentProfile)
class ResidentAdmin(admin.ModelAdmin):
    """ Resident Admin """
    list_display = (
        'pk',
        'building_num',
        'apartment_num',
        'parking_lot_num',
        'property_relation'
    )
