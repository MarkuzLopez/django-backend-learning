
from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializerAuth(serializers.ModelSerializer):
    password =  serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields =  ['username', 'email', 'password']
        
    def create(self, validate_data):
        userAuth = User.objects.create_user(
            username=validate_data['username'],
            email=validate_data.get('email', ''),
            password=validate_data['password']
        )
        return userAuth
    
class LoginSerializerAuth(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'password']