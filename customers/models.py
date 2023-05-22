from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager



class User(AbstractUser):
    PH = 'ph'
    PL = 'pl'
    PT = 'pt'
    BR = 'br'
    CN = 'cn'
    DK = 'dk'
    US = 'us'
    UK = 'uk'
    GR = 'gr'
    CA = 'ca'
    AR = 'ar'
    SA = 'sa'
    BE = 'be'
    COUNTRY_CHOICES = (
        (PH, 'Philippines'),
        (PL, 'Poland'),
        (PT, 'Portugal'),
        (BR, 'Brazil'),
        (CN, 'China'),
        (DK, 'Denmark'),
        (US, 'United States'),
        (UK, 'United Kingdom'),
        (GR, 'Greece'),
        (CA, 'Canada'),
        (AR, 'Argentina'),
        (SA, 'Saudi Arabia'),
        (BE, 'Belgium'),
    )

    ADMIN = 1
    SELLER = 2
    CUSTOMER = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (SELLER, 'Seller'),
        (CUSTOMER, 'Customer'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=CUSTOMER)
    street = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=250, blank=True)
    state = models.CharField(max_length=250, blank=True)
    zip_code = models.CharField(max_length=250, blank=True)
    country = models.CharField(
        max_length=250, blank=True, default=PL, choices=COUNTRY_CHOICES)

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
