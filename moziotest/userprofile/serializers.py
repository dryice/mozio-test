from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import UserProfile, ServiceArea

class UserSerializer(UserDetailsSerializer):

    phone_number = serializers.CharField(source="userprofile.phone_number")
    language = serializers.CharField(source="userprofile.language")
    currency = serializers.CharField(source="userprofile.currency")

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'phone_number', 'language', 'currency')

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile', {})
        phone_number = profile_data.get('phone_number')
        language = profile_data.get('language')
        currency = profile_data.get('currency')

        instance = super(UserSerializer, self).update(instance, validated_data)

        # get and update user profile
        profile, created = UserProfile.objects.get_or_create(
            user = instance)
        
        if profile_data and phone_number:
            profile.phone_number = phone_number
        if profile_data and language:
            profile.language = language
        if profile_data and currency:
            profile.currency = currency

        profile.save()
        return instance


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """
    provider = serializers.ReadOnlyField(source="provider.username")
    
    class Meta:
        model = ServiceArea
        geo_field = "area"

        # you can also explicitly declare which fields you want to include
        # as with a ModelSerializer.
        fields = ('id', 'provider', 'name', 'price')
        read_only_fields = ('provider', )

        
