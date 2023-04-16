from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

class CalcResultSerializer(serializers.Serializer):
    a = serializers.IntegerField()
    b = serializers.IntegerField()
    result = serializers.IntegerField()
    op = serializers.CharField(max_length=1)
