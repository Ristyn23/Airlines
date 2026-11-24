from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from airtickets.models import Aeroport, Flight, Plane, Seat, Ticket
from airtickets.serializers import AeroportSerializer, FlightSerializer, PlaneSerializer, SeatSerializer, TicketSerializer

class AeroportViewSet(
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.ListModelMixin, 
    GenericViewSet
):
    queryset = Aeroport.objects.all()
    serializer_class = AeroportSerializer


class FlightViewSet(
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.ListModelMixin, 
    GenericViewSet
):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PlaneViewSet(
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.ListModelMixin, 
    GenericViewSet
):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer


class SeatViewSet(
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.ListModelMixin, 
    GenericViewSet
):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class TicketViewSet(
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.ListModelMixin, 
    GenericViewSet
):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer