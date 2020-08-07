# -*- coding: utf-8 -*-  

from django.http import HttpResponse,JsonResponse
from api.models import AlertLogrule
from api.lib.serializers import AlertLogruleSerializers
from rest_framework.decorators import api_view
from api.lib.utils import JSONResponse 

@api_view(['GET', 'POST'])
def rules_list(request):
    if request.method == 'GET':
        rules = AlertLogrule.objects.all()
        serializer = AlertLogruleSerializers(rules,many=True)
        return JSONResponse(200,'ok',serializer.data)

    elif request.method == 'POST':
        serializer = AlertLogruleSerializers(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                return JSONResponse(400,'error',str(e))
            return JSONResponse(201,'ok',serializer.data)
        return JSONResponse(400,'error',serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def rules_detail(request,id):
    try:
        rules = AlertLogrule.objects.get(id=id)
    except:
        return JSONResponse(404,'error',safe=False)

    if request.method == 'GET':
        serializer = AlertLogruleSerializers(rules)
        return JSONResponse(200,'ok',serializer.data)

    elif request.method == 'PUT':
        serializer = AlertLogruleSerializers(rules,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(201,'ok',serializer.data)
        return JSONResponse(400,'error',serializer.errors)

    elif request.method == 'DELETE':
        rules.delete()
        return JSONResponse(204,'ok',safe=False)


