from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'bio']
    
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password1 = serializers.CharField(required=True, write_only=True, validators=[validate_password])
    password2 = serializers.CharField(required=True, write_only=True, validators=[validate_password])
    bio = serializers.CharField(required=False)

    def validate(self, data):        
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("password doesn't match.")
        return data

    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            email = validated_data['email'],
        )

        user.set_password(validated_data['password1'])
        user.set_password(validated_data['password2'])

        user.save()
        return user
