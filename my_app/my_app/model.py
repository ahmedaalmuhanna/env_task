

from django.db import models



class Flight(models.Model):
    destination = models.CharField(max_length=100)
    time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    miles = models.PositiveIntegerField()

    def __str__(self):
        return f"to {self.destination} at {self.time}"