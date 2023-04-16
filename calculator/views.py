from django.http import JsonResponse
from .serializers import *
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from calculator import models

# def CalculatorView(request, a, b, op):
#     result = basiccalculator(a, b, op)
#     serializer = CalculatorSerializer(data={'result': result})
#     if serializer.is_valid():
#         return JsonResponse(serializer.data, status=200)
#     return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def calculate(request):
    if request.method == 'POST':
        int1 = int(request.data['a'])
        int2 = int(request.data['b'])
        oper = request.data['op']
        int3 = int1 + int2
        
        r = models.CalcResult()
        r.a = int1
        r.b = int2
        r.op = oper
        r.result = int3
        serializer = CalcResultSerializer(r) 
        # request.data
        return Response({"message": "Calculation done!", "CalcResult": serializer.data})
    return Response({"message": "To use the calculator, do a POST to this url in the json format {a:2,b:3,op:+} and you will get results in the format {'message': 'Calculation done!','CalcResult': {a: 2,b: 31,result: 33,op: +}  }"} )
