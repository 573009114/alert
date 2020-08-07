# -*- coding: utf-8 -*-

from django.http import HttpResponse,JsonResponse
from api.models import AlertLogapp,AlertLogrule
from api.lib.serializers import AppSerializers,AppRuleSerializers
from rest_framework.decorators import api_view
from api.lib.utils import JSONResponse 
import json
from django.core import serializers

@api_view(['GET', 'POST'])
def app_list(request):
    if request.method == 'GET':
        app = AlertLogapp.objects.all()
        serializer = AppSerializers(app,many=True)
        return JSONResponse(200,'ok',serializer.data)
    elif request.method == 'POST':
        serializer = AppSerializers(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                return JSONResponse(400,'error',str(e))
            return JSONResponse(201,'ok',serializer.data)
        return JSONResponse(400,'ok',serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def app_detail(request,id):
    try:
        app = AlertLogapp.objects.get(id=id)
    except:
        return JSONResponse(404,'error')

    if request.method == 'GET':
        app= AlertLogrule.objects.filter(app_id=id).values('app','name','es_index_prefix',
             'es_query','log_count','in_minutes','trigger','product',
             'priority','no_deal','owner')
        return JSONResponse(200,'ok',app,safe=False)

    elif request.method == 'PUT':
        serializer = AppSerializers(app,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(201,'ok',serializer.data)
        return JSONResponse(400,'error',serializer.errors)
    elif request.method == 'DELETE':
        app.delete()
        return JSONResponse(204,'ok')
