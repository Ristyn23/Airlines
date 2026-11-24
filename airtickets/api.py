from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate

from airtickets.models import Aeroport, Flight, Plane, Seat, Ticket, Profile
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



class ProfileViewSet(GenericViewSet):
    queryset = User.objects.all()

    @action(detail=False, url_path="me", methods=['GET'])
    def get_me(self, request, *args, **kwargs):
        data = {
            'is_authenticated': self.request.user.is_authenticated
        }

        if self.request.user.is_authenticated:
            data.update({
                "username": self.request.user.username,
                "id": self.request.user.id,
                "role": self.request.user.profile.role,
            })

        return Response(data=data)

    @action(detail=False, url_path="logout", methods=['POST'])
    def logout(self, *args, **kwargs):
        django_logout(self.request)

        return Response()

    @action(detail=False, url_path="login", methods=['POST'])
    def login(self, *args, **kwargs):
        username = self.request.data['username']
        password = self.request.data['password']

        success = False
        status_code = 403

        user = authenticate(username=username, password=password)
        if user:
            success = True
            status_code = 200
            django_login(self.request, user)

        return Response({
            'success': success
        }, status=status_code)

    @action(detail=False, url_path="register", methods=['POST'])
    def register(self, *args, **kwargs):
        username = self.request.data['username']
        password = self.request.data['password']
        User.objects.create_user(
            username=username,
            password=password,
        )

        return Response()

    @action(detail=False, url_path="activate_user", methods=['POST'])
    def activate_user(self, *args, **kwargs):
        pass