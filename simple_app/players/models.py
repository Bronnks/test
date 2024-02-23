from django.db import models

from vehicles.models import Tank


class Players(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=150)
    date_joined = models.DateTimeField()


class PlayerVehicles(models.Model):
    player_id = models.ForeignKey(Players, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Tank, on_delete=models.CASCADE)
    experience_points = models.IntegerField()
