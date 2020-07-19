from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Repair(models.Model):
    DEVICES_CHOICES = (
        ('iPhone 11 Pro', 'iPhone 11 Pro'),
        ('Samsung Galaxy S20', 'Samsung Galaxy S20'),
        ('Samsung Galaxy Note 10+', 'Samsung Galaxy Note 10+'),
        ('Samsung Galaxy Note 10', 'Samsung Galaxy Note 10'),
        ('iPhone 11 Pro Max', 'iPhone 11 Pro Max'),
        ('iPhone 11', 'iPhone 11 '),
        ('Samsung Galaxy S20+', 'Samsung Galaxy S20+'),
        ('Samsung Galaxy S20 Ultra', 'Samsung Galaxy S20 Ultra'),
    )
    BUGS_CHOICES = (
        ('Broken Screen', 'Broken Screen'),
        ('Broken Back', 'Broken Back'),
        ('Not Charging', 'Not Charging'),
        ('Broken', 'Broken'),
        ('Total Lost', 'Total Lost'),      
    )
    BRAND_CHOICES = (
        ('Apple', 'Apple'),
        ('Samsung', 'Samsung'),
        ('Xioami', 'Xioami'),
        ('LG', 'LG'),
             
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) #relationship 1:n (user:todos)
    dateCreated = models.DateField(auto_now_add=True) #automatic
    dateCompleted = models.DateField(null=True, blank=True) #blank at first
    Device = models.CharField(max_length=70, choices = DEVICES_CHOICES)
    description = models.TextField(blank=True)
    bug = models.CharField(max_length=70, choices = BUGS_CHOICES)
    brand = models.CharField(max_length=70, choices = BRAND_CHOICES)
def __str__(self):
    return self.Device
