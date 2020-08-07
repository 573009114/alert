from django.http import HttpResponse
from api.models import AlertNotice
from api.lib.serializers import NoticeSerializers
from rest_framework.decorators import api_view
from api.lib.utils import JSONResponse 


@api_view(['GET', 'POST'])
def notice_list(request):
    if request.method == 'GET':
        notice = AlertNotice.objects.all()
        serializer = NoticeSerializers(notice,many=True)
        return JSONResponse(200,'ok',serializer.data)
    elif request.method == 'POST':
        serializer = NoticeSerializers(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                return JSONResponse(400,'error',str(e))
            return JSONResponse(201,'ok',serializer.data) 
        return JSONResponse(400,'error',serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def notice_detail(request,id):
    try:
        notice = AlertNotice.objects.get(id=id)
    except:
        return JSONResponse(404,'error')

    if request.method == 'GET':
        serializer = NoticeSerializers(notice)
        return JSONResponse(200,'ok',serializer.data)
    elif request.method == 'PUT':
        serializer = NoticeSerializers(notice,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(201,'ok',serializer.data)
        return JSONResponse(400,'error',serializer.errors)
    elif request.method == 'DELETE':
        notice.delete()
        return JSONResponse(204,'ok')
  
