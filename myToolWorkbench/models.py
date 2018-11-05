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

'''
class Days(models.Model):
    DAYS = (
        ('Mon', 'Monday'),
        ('Tues', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thurs', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    )
    days_visited = models.CharField(max_length=4, choices=DAYS)
'''


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name, self.last_name


class Business(models.Model):
    DAYS = (
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    )
    name = models.CharField(max_length=50)
    address = models.CharField(max_length= 128)
    owner_first = models.CharField(max_length=30)
    owner_last = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    day_visited = models.CharField(max_length=3, choices=DAYS)
    employees = models.ManyToManyField(Person, through='Employed')

    def __str__(self):
        return self.name


class Employed(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)


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