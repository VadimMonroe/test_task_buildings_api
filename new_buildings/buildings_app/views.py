from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import BuildingsBase
from .serializers import BuildingsSerializer
from .logic import plus


def index(request):
    context = plus(2, 3)
    return render(request, 'buildings_app/index.html', {'context': context})


class BuildingsApiView(generics.ListCreateAPIView):
    queryset = BuildingsBase.objects.all()
    serializer_class = BuildingsSerializer


class BuildingApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuildingsBase.objects.all()
    serializer_class = BuildingsSerializer
