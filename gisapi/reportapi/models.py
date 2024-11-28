from django.db import models
from datetime import datetime

class User(models.Model):
    user_name: str = models.CharField(max_length=255, verbose_name="Nome do Usuário")
    user_email: str = models.EmailField(verbose_name="Email do Usuário")
    user_car_cod: str = models.CharField(max_length=50, verbose_name="Código CAR")
    user_reg_date: datetime = models.DateTimeField(auto_now_add=True, verbose_name="Data de Registro")

    def __str__(self) -> str:
        return f"{self.user_name} - {self.user_email}"
    
    