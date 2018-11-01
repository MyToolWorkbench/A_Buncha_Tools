from django.db import models
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
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)


class User(Person):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class Tool(models.Model):
    part_number = models.CharField(max_length=30)
    description = models.TextField()
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    special_retail = models.DecimalField(max_digits=7, decimal_places=2)
    regular_retail = models.DecimalField(max_digits=7, decimal_places=2)
    # catalogue_page
    # tw_page
    # UOM
    upc_code = models.IntegerField()
    weight = models.DecimalField(max_digits=7, decimal_places=2)
    length = models.DecimalField(max_digits=7, decimal_places=2)
    width = models.DecimalField(max_digits=7, decimal_places=2)
    height = models.DecimalField(max_digits=7, decimal_places=2)
    # origin_country

"""
Business:
Address 
Owner
Phone #
Day(s) of visit
"""