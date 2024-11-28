from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from datetime import datetime

def index(request):
    data_hora = datetime.now().strftime("%x %X")
    return render(request, 'index.html', {'data_hora': data_hora})