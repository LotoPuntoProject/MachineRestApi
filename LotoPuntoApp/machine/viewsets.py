from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from .models import LotoMachine

from .serializer import LotoMachineSerializer

class LotoMAchineViewSet(viewsets.ModelViewSet):
    queryset = LotoMachine.objects.all()
    serializer_class = LotoMachineSerializer
    # @action(detail=True, methods=['get'])
    # def elements(self, request, pk=None):
    #     queryset = LotoMachine.objects.filter(category_id=pk)
    #     serializer = LotoMachineSerializer(queryset, many=True)
    #     return Response(serializer.data)