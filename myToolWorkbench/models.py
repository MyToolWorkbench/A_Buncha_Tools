from django.db import models
from django.contrib.auth.models import User
from enum import Enum
# Create your models here.

""""
class Country(Enum):
    USA = "USA"
    CHINA = "CHN"
    TAIWAN = "TWN"
    INDONESIA = "IDN"
    MALAYSIA = "MAL"

"""


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=30)
    email_address = models.EmailField(default='default@email.com')


class UserAccount(Person):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Tool(models.Model):
    part_number = models.CharField(max_length=30)
    description = models.TextField(default="")
    cost = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True)
    special_retail = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True)
    regular_retail = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True)
    upc_code = models.CharField(max_length=30, null=True)
    weight = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True)
    length = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True)
    width = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True)
    height = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True)
    origin_country = models.CharField(max_length=10, null=True)
