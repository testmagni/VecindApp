# Import Django User model
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=25, unique=True, blank=True)
    NOT_DEFINED = 1
    WATCHMAN = 2
    RESIDENT = 3
    ROLE_CHOICES = (
        (NOT_DEFINED, 'No Definido'),
        (WATCHMAN, 'Celador'),
        (RESIDENT, 'Residente'),
    )
    user_role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=NOT_DEFINED)


class Watchman(models.Model):
    """ Define el modelo de Watchman, el cual será una extensión del modelo User
        que hereda de CommonInfo.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user_watchman',
        null=True
    )
    id_num = models.PositiveSmallIntegerField(blank=False, unique=True, null=True)

    # Meta Data
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name + self.user.last_name


class Resident(models.Model):
    """ Define el modelo de Resident, el cual será una extensión del modelo User
        que hereda de CommonInfo.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user_resident',
        null=True,
    )
    OWNER = 1
    TENANT = 2
    RELATION_W_PROPERTY = (
        (OWNER, 'PROPIETARIO'),
        (TENANT, 'ARRENDATARIO')
    )
    building_num = models.PositiveSmallIntegerField(blank=True, null=True)
    apartment_num = models.PositiveSmallIntegerField(blank=True, null=True)
    parking_lot_num = models.PositiveSmallIntegerField(blank=True, null=True)
    property_relation = models.PositiveSmallIntegerField(
        choices=RELATION_W_PROPERTY,
        default=TENANT,
        blank=False,
    )

    # Meta Data
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name + self.user.last_name
