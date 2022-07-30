from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import UploadSerializer

class StatusView(APIView):
  
   def get(self, request):
       return Response({'result':'server is running and OK'}, status=status.HTTP_200_OK)


class FileUploadView(APIView):
    
    serializer_class = UploadSerializer

    def get(self, request):
        return Response("GET Method")

    def post(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        f = file_uploaded.open()
        content_type = file_uploaded.content_type
        response = {'result':'file uploaded successfully', 'content_type':content_type, 'value':f.read()}
        return Response(response)
 
@api_view(['GET', 'POST'])
def hello_world(request):
   if request.method == 'POST':
       return Response({"message": "Got some data!", "data": request.data})
   return Response({"message": "Hello, world!"})