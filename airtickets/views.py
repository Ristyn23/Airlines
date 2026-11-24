from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from airtickets.models import Aeroport

# Create your views here.
class AeroportListView(View):
    def get(request, *args, **kwargs):
        aeroport = list(Aeroport.objects.all().values())
        return JsonResponse({
            'data': aeroport,
        })