from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

# Render the most descendant extension template to render it and all
def home(request):
    return render(request, 'results.html', {})


# Endpoint for getting user input
def user_data(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")

        return JsonResponse({'message': 'User data submitted.'})
    else:
        return JsonResponse({'error': 'Invalid request'})