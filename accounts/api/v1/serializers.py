from rest_framework import serializers
from ...models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions



class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255, write_only=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password1']:
            raise serializers.ValidationError("Passwords don't match")
        try :
            validate_password(attrs.get('password'))
        except exceptions.ValidationError as e :
            raise serializers.ValidationError({'error': list(e.messages)})
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop('password1', None)
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('email', 'password', 'password1')