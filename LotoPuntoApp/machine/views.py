from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404
import requests

from .models import LotoMachine

from .serializer import LotoMachineSerializer

import json

def index(request):
    return HttpResponse("Loto Punto App")

def login_request(user, password, terminalId):
    url = 'http://demo4885696.mockable.io/loto-punto/login'
    user = 'noreplycincop@gmail.com'
    password = 'XQW8UbVDwZ'
    payload = {"user": user, "password": password, "terminalId": terminalId}
    return requests.post(url, json=payload)


# Create your views here.
@api_view(['GET'])
def autologin(request, ):
    if request.method == 'GET':
        try:
            queryset = LotoMachine.objects.get(pk=1)
        except LotoMachine.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # user = get_object_or_404(queryset, pk=pk)
        serializer = LotoMachineSerializer(queryset)
        data = serializer.data
        ans  = login_request(data['user'], data['password'], data['terminalId'])
        status = ans.status_code
        data_ans = json.loads(ans.text)
        
        print(f"Respuesta del request: {ans.text} {type(ans.text)} status: {status}")
        print(f"Respuesta del request: {data_ans} {type(data_ans)} status: {status}")
        # data = data.__dict__
        print(f"data: {data['user']} type: {type(data)}")
        return JsonResponse(data_ans)
        # return ans.text
        # snippets = Snippet.objects.all()
        # serializer = SnippetSerializer(snippets, many=True)
        # return Response("hello")

    elif request.method == 'POST':
        pass
        # serializer = SnippetSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
