from django.db import models

# Create your models here.

from django.db import models

class Register(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, null=True, blank=True)
    dob = models.DateField(null=False, blank=False)
    birthplace = models.CharField(max_length=100,null=False, blank=False)
    education = models.CharField(max_length=100,null=False, blank=False)

    def __str__(self):
        return self.email