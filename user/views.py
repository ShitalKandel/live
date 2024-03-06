from rest_framework.views import APIView
from user.serializers import UserSerializer


class UserView(APIView):
    serialzer = UserSerializer
    serialzer.save()


    

