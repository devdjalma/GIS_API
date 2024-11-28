from django.urls import path
from . import views

# Padrões de URLS que o user vai navegar
urlpatterns = [
    path("", views.index)
]
