from django.http import HttpResponse
from api.models import AlertEvent
from api.lib.serializers import EventSerializers
from rest_framework.decorators import api_view
from api.lib.utils import JSONResponse 


@api_view(['GET', 'POST'])
def event_list(request):
    if request.method == 'GET':
        event = AlertEvent.objects.all()
        serializer = EventSerializers(event,many=True)
        return JSONResponse(200,'ok',serializer.data)
    elif request.method == 'POST':
        serializer = EventSerializers(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                return JSONResponse(400,'error',str(e))
            return JSONResponse(201,'ok',serializer.data)
        return JSONResponse(400,'error',serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def event_detail(request,id):
    try:
        event = AlertEvent.objects.get(id=id)
    except:
        return JSONResponse(404,'error')

    if request.method == 'GET':
        serializer =  EventSerializers(event)
        return JSONResponse(200,'ok',serializer.data)
    elif request.method == 'PUT':
        serializer = EventSerializers(event,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(201,'ok',serializer.data)
        return JSONResponse(400,'error',serializer.errors)
    elif request.method == 'DELETE':
        event.delete()
        return JSONResponse(204,'ok')
  
