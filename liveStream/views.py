from liveStream.serializers import ArtistSerializer,FileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from liveStream.models import ArtistModel,FileModel
from django.http import FileResponse
import os
from rest_framework.parsers import MultiPartParser


class ArtistView(APIView):
    def post(self,requset,*args,**kwargs):
        serializer = ArtistSerializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,({
            'status':404,
            'message':'Not Found'
        }))
    
    def get(self,request):
        queryset = ArtistModel.objects.all()
        serialzer = ArtistSerializer(queryset,many=True)
        return Response(serialzer.data,status=status.HTTP_200_OK)


class FileView(APIView):
    parser_classes = [MultiPartParser]

    def post(self,request,*args,**kwargs):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, audio_id, *args, **kwargs):
        try:
            audio = FileModel.objects.get(id=audio_id)
            return FileResponse(open(audio.upload_file.path, 'rb'))
        except FileModel.DoesNotExist:
            return Response({"error": "Audio not found"}, status=status.HTTP_404_NOT_FOUND)
            