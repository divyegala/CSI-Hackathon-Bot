from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import requests

@api_view(['GET'])
def luis(request):
    q = request.GET.get('q', '')
    print(q)
    return Response("done")
