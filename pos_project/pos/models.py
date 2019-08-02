from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Customer(models.Model):
    phone_number = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    address_1 = models.CharField(max_length=30, blank=True)
    address_2 = models.CharField(max_length=30, blank=True)
    zip_code = models.CharField(max_length=5)
    city = models.CharField(max_length=20)
    business_name = models.CharField(max_length=30)
    ext = models.CharField(max_length=15, blank=True)
    room = models.CharField(max_length=10)
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.phone_number


class MenuCategory(models.Model):
    category01 = models.CharField(max_length=15)


class MenuModifer(models.Model):
    pass


class MenuItem(models.Model):
    menucategory = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    modifiers = models.ManyToManyField(MenuModifer)
    item = models.CharField(max_length=15)
    price = models.CharField(max_length=5)



