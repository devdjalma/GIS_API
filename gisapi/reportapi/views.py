from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.


def processo_car_code(request, code):
    if request.method == "GET":
        pass
        if code == "ms01":
	    reponse = {"status":"sucess", "message":"FOi!"}
        else:
    	    reponse = {"status":"fail", "message":"Not"}
        return JsonResponse(response)
    else:
	return JsonResponde("status":"fail", "message":"Metodo bugado!"})
