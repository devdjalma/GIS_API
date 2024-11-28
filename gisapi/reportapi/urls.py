from django.urls import path
from .views import user_form_view

urlpatterns = [
    path('form/', user_form_view, name='user_form'),
]
