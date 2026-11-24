from django.contrib import admin
from .models import Aeroport, Plane, Flight, Profile, Seat, Ticket

@admin.register(Aeroport)
class AeroportAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'country', 'iata_code']

@admin.register(Plane)
class PlaneAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'board_number']

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'depature_date', 'depature_time', 'arrival_date', 'arrival_time', 'depature_aeroport', 'arrival_aeroport', 'plane']

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ['id', 'plane', 'row_number', 'seat_letter'] 

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'flight', 'seat', 'price', 'purchase_date']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False