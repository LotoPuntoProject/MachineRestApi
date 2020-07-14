from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404
import requests

from .models import LotoMachine

from .serializer import LotoMachineSerializer

def index(request):
    return HttpResponse("Loto Punto App")

def login_request(user, password, terminalId):
    url = ''
    payload = {"user": user, "password": password, "terminalId": terminalId}
    ans = requests.post(url, data=payload)

# Create your views here.
@api_view(['GET'])
def autologin(request):
    if request.method == 'GET':
        pass
        # snippets = Snippet.objects.all()
        # serializer = SnippetSerializer(snippets, many=True)
        return Response("hello")

    elif request.method == 'POST':
        pass
        # serializer = SnippetSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
