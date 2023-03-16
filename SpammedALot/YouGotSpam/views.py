from django.shortcuts import render
from django.http import JsonResponse
import json

# user dictionary
user_info = {
    'email': '',
    'password': ''
}

# Render the most descendant extension template to render it and all
def home(request):
    return render(request, 'results.html', {})


# Endpoint for getting user input
def user_data(request):
    # process the data from JavaScript
    if request.method == "POST":
        data = json.loads(request.body)
        # set data
        user_info['email'] = data.get("email"),
        user_info['password'] = data.get("password")
        return JsonResponse({'message': 'User data submitted!'})
    elif request.method == "GET":
        # send data for JavaScript to consume
        return JsonResponse(user_info)
    else:
        return JsonResponse({'error': 'Invalid request'})