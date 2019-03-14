# Import Django User model
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=25, blank=True)
    RESIDENT = 1
    WATCHMAN = 2
    NOT_DEFINED = 3
    ROLE_CHOICES = (
        (NOT_DEFINED, 'No Definido'),
        (WATCHMAN, 'Vigilante'),
        (RESIDENT, 'Residente'),
    )
    user_role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=NOT_DEFINED)


class WatchmanProfile(models.Model):
    """ Define el modelo de Watchman, el cual será una extensión del modelo User
        que hereda de CommonInfo.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='w_profile',
        null=True
    )
    id_num = models.PositiveSmallIntegerField(blank=False, unique=True, null=True)

    # Meta Data
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name + self.user.last_name


class ResidentProfile(models.Model):
    """ Define el modelo de Resident, el cual será una extensión del modelo User
        que hereda de CommonInfo.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='r_profile',
        null=True,
    )
    OWNER = 1
    TENANT = 2
    NOT_DEFINED = 3
    RELATION_W_PROPERTY = (
        (OWNER, 'PROPIETARIO'),
        (TENANT, 'ARRENDATARIO'),
        (NOT_DEFINED, 'NO DEFINIDO')
    )
    building_num = models.PositiveSmallIntegerField(blank=True, null=True)
    apartment_num = models.PositiveSmallIntegerField(blank=True, null=True)
    parking_lot_num = models.PositiveSmallIntegerField(blank=True, null=True)
    property_relation = models.PositiveSmallIntegerField(
        choices=RELATION_W_PROPERTY,
        default=NOT_DEFINED,
        blank=False,
    )

    # Meta Data
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name + self.user.last_name
