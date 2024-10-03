from rest_framework import viewsets
from cars.models import Brand, Car
from cars.serializers import BrandModelSerializer, CarModelSerializer


class BrandModelViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandModelSerializer


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarModelSerializer
