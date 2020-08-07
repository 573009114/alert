from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
import json

class JSONResponse(JsonResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self,status='null',msg='null',data='null',**kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        response =dict()
        response['status']=status
        response['msg']=msg
        response['data']=json.loads(content)
       
        return super(JSONResponse, self).__init__(response,**kwargs)

