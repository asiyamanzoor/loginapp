from django.db import models

# Create your models here.
class Customer(models.Model):
    user_id = models.BigAutoField
    #first_name = models.CharField(max_length = 50, default ="")
    #last_name = models.CharField(max_length = 50, default ="", null = 'False')
    user_name = models.CharField(max_length = 50, default ="")
    password = models.CharField(max_length = 59,default="")

def __str__(self):
    return self.user_name

class Doctor(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length = 50, default ="")
    last_name = models.CharField(max_length = 50, default ="", null = 'False')
    user_name = models.CharField(max_length = 50, default ="")
    password = models.CharField(max_length = 59,default="")

def __str__(self):
    return self.first_name