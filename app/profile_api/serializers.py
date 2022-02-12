from rest_framework import serializers

from profile_api import models


class HelloSerializer(serializers.Serializer):
    """Serializer for name field for testing APIView"""

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes User profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id' , 'email', 'name', 'password')
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style" : {
                    "input-type": "password"
                }
            }
        }
    

    def create(self, validated_data):
        """create and return a new user"""

        user = models.UserProfile.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            password= validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """to update user"""

        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        
        return super().update(instance, validated_data)