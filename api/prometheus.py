from django.http import HttpResponse
from api.models import AlertPrometheus
from api.lib.serializers import PrometheusSerializers
from rest_framework.decorators import api_view
from api.lib.utils import JSONResponse 


@api_view(['GET', 'POST'])
def prometheus_list(request):
    if request.method == 'GET':
        prometheus = AlertPrometheus.objects.all()
        serializer = PrometheusSerializers(prometheus,many=True)
        return JSONResponse(200,'ok',serializer.data)
    elif request.method == 'POST':
        serializer = PrometheusSerializers(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                return JSONResponse(400,'error',str(e))
            return JSONResponse(201,'ok',serializer.data)
        return JSONResponse(400,'error',serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def prometheus_detail(request,id):
    try:
        prometheus = AlertPrometheus.objects.get(id=id)
    except:
        return JSONResponse(404,'error')

    if request.method == 'GET':
        serializer = PrometheusSerializers(prometheus)
        return JSONResponse(200,'ok',serializer.data)
    elif request.method == 'PUT':
        serializer = PrometheusSerializers(prometheus,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(201,'ok',serializer.data)
        return JSONResponse(400,'error',serializer.errors)
    elif request.method == 'DELETE':
        prometheus.delete()
        return JSONResponse(204,'ok')
  
