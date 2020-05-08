from django.db import models

# Create your models here.
class Destinaion(models.Model):
    Type=(
        ('INTERNATIONAL','INTERNATIONAL'),('DOMESTIC','DOMESTIC')
        )

    name = models.CharField(max_length = 255)
    days = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pics')
    tourtype=models.CharField(max_length=20,choices=Type)


class CustomerReview(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    review=models.CharField(max_length=255)
    image = models.ImageField(upload_to='pics')

