from django.db import models


# Create your models here.
class Location(models.Model):

    city = models.CharField(max_length=100)
    country = models.CharField(max_length=90)
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.country} -> {self.city}"


class AuditLocation(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=90)
    active = models.BooleanField(default=1)
    location = models.IntegerField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.country} -> {self.city}"
