from rest_framework import serializers

from .models import LotoMachine


class AutoLogin(object):
    def __init__(self, authorizationToken, permissions):
        self.authorizationToken = authorizationToken
        self.permissions = permissions

class LotoMachineSerializer(serializers.ModelSerializer):

    class Meta:
        model = LotoMachine
        fields = ['user', 'password', 'terminalId']

class AutoLoginSerializer(serializers.Serializer):
    authorizationToken = serializers.CharField(max_length=200)
