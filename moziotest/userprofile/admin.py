from django.contrib.gis import admin
from .models import UserProfile, ServiceArea

admin.site.register(UserProfile, admin.ModelAdmin)
admin.site.register(ServiceArea, admin.GeoModelAdmin)
