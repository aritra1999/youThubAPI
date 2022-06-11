import json

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes

from .utils import yt_init

def index(request): 
    data = {
        "hello": "World"
    } 
    return JsonResponse(data)

@api_view(['POST'])
@permission_classes([])
def process_view(request):
    data = json.loads(request.body)
    comments = yt_init(data["link"])
    return JsonResponse({
        "comments": comments
    })
        


    

