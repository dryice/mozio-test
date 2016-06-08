from rest_framework import generics, viewsets
from rest_framework import permissions

from .models import ServiceArea
from .serializers import ServiceAreaSerializer
from .filters import ServiceAreaFilter


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.provider == request.user


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """
    Service Area CRUD.

    When creating/updating, the area parameter should be a
    polygon. E.g:
    
    {
        "type": "Polygon",
        "coordinates": [
            [
                [
                    17.75390625,
                    8.2265630364418
                ],
                [
                    22.587890625,
                    4.09
                ],
                [
                    12.744140625,
                    -1.5292963385582
                ],
                [
                    12.392578125,
                    6.5566411614418
                ],
                [
                    13.798828125,
                    10.687500536442
                ],
                [
                    16.34765625,
                    10.687500536442
                ],
                [
                    17.75390625,
                    8.2265630364418
                ]
            ]
        ]
    }

    When quering, the contains_point parameter should be a point
    (lat/lng pair). E.g:

    { "type": "Point", "coordinates": [ 14, 4 ] }
    """    
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    filter_class = ServiceAreaFilter
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    
    def perform_create(self, serializer):
        serializer.save(provider=self.request.user)
