from django.db import models

# Create your models here.
class Aeroport(models.Model):
    name = models.TextField()
    city = models.TextField()
    country = models.TextField()
    iata_code = models.TextField()

class Flight(models.Model):
    number = models.TextField()
    depature_date = models.DateField()
    depature_time = models.TimeField()
    arrival_date = models.DateField()
    arrival_time = models.TimeField()
    depature_aeroport = models.ForeignKey("airtickets.Aeroport", on_delete=models.CASCADE, null=True, related_name='departure_flights')
    arrival_aeroport = models.ForeignKey("airtickets.Aeroport", on_delete=models.CASCADE, null = True, related_name='arrival_flights')
    plane = models.ForeignKey("airtickets.Plane", on_delete=models.CASCADE, null=True)

class Plane(models.Model):
    model = models.TextField()
    board_number = models.TextField()

class Seat(models.Model):
    plane = models.ForeignKey("Plane", on_delete=models.CASCADE)
    row_number = models.IntegerField()
    seat_letter = models.TextField()

class Ticket(models.Model):
    client = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True)
    flight = models.ForeignKey("airtickets.Flight", on_delete=models.CASCADE, null=True)
    seat = models.ForeignKey("airtickets.Seat", on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()