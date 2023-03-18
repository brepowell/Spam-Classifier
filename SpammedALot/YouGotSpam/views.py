from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import Profile
profiles = Profile.objects.all()

# user dictionary
user_info = {
    'user': '',
    'name': '',
    'email': '',
    'password': '' 
}

# Render the most descendant extension template to render it and all
def home(request):
    return render(request, 'results.html', {})

# Endpoint for getting full user input 
def user_data(request):
    # process the data from JavaScript
    if request.method == "POST":
        data = json.loads(request.body)
        # input data
        rec_user = data.get("user")
        rec_name = data.get("name")
        rec_email = data.get("email")
        rec_password = data.get("password")

        # TODO: connect data to Model somehow - store email address & password?

        # For testing purposes, use user_info dictionary:
        # user_info.clear() # clear first

        user_info['user'] = rec_user
        user_info['name'] = rec_name
        user_info['email'] = rec_email
        user_info['password'] = rec_password
        return JsonResponse({'message': 'User data submitted!'})
    # send processed data for JavaScript to consume
    elif request.method == "GET":

        # TODO: connect data to Model, JSONify data then send back to JS


        return JsonResponse(user_info)
    else:
        return JsonResponse({'error': 'Invalid request'})
