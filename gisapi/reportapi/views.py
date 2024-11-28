from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from typing import Any, Dict

@csrf_exempt
def user_form_view(request) -> JsonResponse:
    if request.method == 'POST':
        name: str = request.POST.get('user-name', '')
        email: str = request.POST.get('user-email', '')
        car_cod: str = request.POST.get('texto', '')

        # Placeholder function
        def placeholder_calculation(cod: str) -> Dict[str, Any]:
            return {"resultado": len(cod) * 10, "status": "Sucesso"}

        calc_result = placeholder_calculation(car_cod)

        # Save user to the database
        user = User(user_name=name, user_email=email, user_car_cod=car_cod)
        user.save()

        # Return JSON response
        return JsonResponse({
            "user": UserSerializer(user).data,
            "calculation": calc_result
        }, status=201)

    return JsonResponse({"error": "Invalid request method"}, status=400)
