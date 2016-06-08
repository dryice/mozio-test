from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis import filters
import django_filters

from .models import ServiceArea


class ServiceAreaFilter(GeoFilterSet):
    contains_point = filters.GeometryFilter(name='area', lookup_type='contains')
    
    class Meta:
        model = ServiceArea
        fields = ("price", "contains_point")
