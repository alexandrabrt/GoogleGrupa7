from rest_framework import viewsets

from api.serializers import LocationSerializers
from aplicatie1.models import Location


# Create your views here.
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('city')
    serializer_class = LocationSerializers
