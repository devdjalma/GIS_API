from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_name', 'user_email', 'user_car_cod', 'user_reg_date']
