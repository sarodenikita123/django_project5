from django.db import models


class Hotel(models.Model):
    Gender = [("MEN", "men"), ("WOMEN", "women"), ("OTHER", "other")]
    name = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    booking_date_time = models.DateField()
    aadhar_no = models.IntegerField()
    type = models.CharField(max_length=20, choices=Gender)
    created_at = models.DateField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True)
