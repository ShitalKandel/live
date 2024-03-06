from rest_framework import serializers
from user.models import UserModel
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class UserSerializer(serializers.ModelSerializer):

    permission_classes = [IsAuthenticated]
    def post(self,request,*args,**kwargs):
        qs = UserModel.objects.all()
        serializer = UserSerializer(qs,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            Response('index.html',{'message':'Account Created Successfully'},status=status.HTTP_201_CREATED)
    class Meta:
        model = UserModel
        fields = '__all__'

    def get(self,requset):
        pass



