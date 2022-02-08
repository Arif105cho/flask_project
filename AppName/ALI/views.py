from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView,ListCreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import *
from ..models import *
from rest_framework.status import *
from rest_framework.filters import SearchFilter
from rest_framework.mixins import CreateModelMixin,ListModelMixin,UpdateModelMixin


##These are using generic ListaPi and other model classes
class CreateUser(CreateAPIView):
    queryset = SignUp.objects.all()
    permission_class = AllowAny
    serializer_class = SignUpSerializer

class ListUser(ListAPIView):
    queryset = SignUp.objects.all()
    permission_class = AllowAny
    serializer_class = SignUpSerializer

class UpdateUser(UpdateAPIView):
    queryset = SignUp.objects.all()
    permission_class = AllowAny
    serializer_class = SignUpSerializer


class DeleteUser(DestroyAPIView):
    queryset = SignUp.objects.all()
    permission_class = AllowAny
    serializer_class = SignUpSerializer

class CreateUser1(APIView):
    def post(self, request, format=None):
        serializer=SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":'user created successfully'},status=HTTP_201_CREATED)
        else:
            return Response({'message':'something wrong','error':serializer.errors},status=HTTP_400_BAD_REQUEST)
class LoginClass(APIView):
    def post(self, request, format=None):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"User":'Login  successfully'},status=HTTP_201_CREATED)

        return Response({'message':'something wrong','error':serializer.errors},status=HTTP_400_BAD_REQUEST)

