from django.shortcuts import render # type: ignore
from django.http import JsonResponse # type: ignore


# Create your views here.


def processo_car_code(request, code):
    if request.method == "GET":
        # PROCESSAR O CÓDIGO RECEBIDO AQUI
        if code == "ms01":
            response = {"status":"sucess", "message":"FOi!"}
        else:
            response = {"status":"fail", "message":"Not"}
        return JsonResponse(response)
    else:
        return JsonResponse({"status":"fail", "message":"Metodo bugado!"})
