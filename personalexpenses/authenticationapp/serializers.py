from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class LoginSerializer(serializers.Serializer):
   email = serializers.EmailField()
   password = serializers.CharField(write_only=True)


class UserRegisterSerializer(serializers.ModelSerializer):
   password = serializers.CharField(write_only=True)
  
   class Meta:
       model = User
       fields = ['email', 'password', 'username']
  
   def create(self, validated_data):
       user = User.objects.create_user(
           email=validated_data['email'],
           password=validated_data['password'],
           username=validated_data['username']
       )
       return user
  
   def validate_email(self, value):
       user = User.objects.filter(email=value).first()
       if user:
           raise ValidationError('Este e-mail já está em uso!')
       return value