from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=64)
    user_email = models.CharField(max_length=64)
    user_car_cod = models.CharField(max_length=64)
    user_reg_date = models.DateTimeField(auto_created=True)
    
