from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def get_list(request):
    data = {
        "message": "Welcome to the API!",
        "items": [1, 2, 3, 4, 5]
    }
    return Response(data)