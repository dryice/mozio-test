from rest_framework import generics, viewsets

from .models import ServiceArea
from .serializers import ServiceAreaSerializer

# class ServiceAreaList(generics.ListCreateAPIView):
#     queryset = ServiceArea.objects.all()
#     serializer_class = ServiceAreaSerializer

# class ServiceAreaDetail(genrics.RetriveUpdateDestroyAPIView):
#     queryset = ServiceArea.objects.all()
#     serializer_class = ServiceAreaSerializer

class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    
