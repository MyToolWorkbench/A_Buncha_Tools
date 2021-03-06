from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Used to describe customers and mTW users.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=30)
    email_address = models.EmailField(default='default@email.com')
    address = models.CharField(max_length=150, default='no address')

    def __str__(self):
        return self.first_name, self.last_name


# Extends Person and links information to an authenticated user
class UserAccount(Person):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


# Businesses users sell to/contract with
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
    address = models.CharField(max_length=128)
    owner_first = models.CharField(max_length=30)
    owner_last = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    day_visited = models.CharField(max_length=3, choices=DAYS)
    employees = models.ManyToManyField(Person, through='Employed')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by', default=1)

    def __str__(self):
        return self.name


# Connector class, connects Business object and client(Person)
class Employed(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)



# Tool template, allows quick creation of tool instances
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


# Tool inventory assigned to a user
class Workbench(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)


# For tools created by users when tool template does not have the required tool
class CustomTool(Tool):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


# Unique instance of tool, belongs to a Workbench and references a Tool or CustomTool object
class ToolInstance(models.Model):
    custom = models.BooleanField(default=False)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, null=True)
    inventory = models.ForeignKey(Workbench, on_delete=models.CASCADE, default=1)


