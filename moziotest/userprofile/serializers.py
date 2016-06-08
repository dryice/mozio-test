from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer

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
        profile = instance.userprofile
        if profile_data and phone_number:
            profile.phone_number = phone_number
        if profile_data and language:
            profile.language = language
        if profile_data and currency:
            profile.currency = currency

        profile.save()
        return instance
