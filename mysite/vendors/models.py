from django.db import models
from core.models import TimeStampedModel


class Vendor(TimeStampedModel):
    name = models.TextField(max_length=50)

    def __str__(self):
        return self.name


class VendorEmail(TimeStampedModel):
    vendor = models.ForeignKey(to=Vendor, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'

    def __str__(self):
        return self.email


class VendorPhoneNumber(TimeStampedModel):
    vendor = models.ForeignKey(to=Vendor, on_delete=models.CASCADE)
    phone_number = models.TextField(unique=True, max_length=10)

    class Meta:
        verbose_name = 'Phone Number'
        verbose_name_plural = 'Phone Numbers'

    def __str__(self):
        return self.phone_number
