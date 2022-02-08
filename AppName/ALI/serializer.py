from rest_framework.serializers import ModelSerializer
from ..models import SignUp,Login
from rest_framework.serializers import *
from rest_framework.response import Response


class SignUpSerializer(ModelSerializer):

    class Meta:
        model=SignUp
        fields=('__all__')
class LoginSerializer(Serializer):
    email = CharField(error_messages={'required': 'email is required', 'blank': 'email is required'})
    password = CharField(error_messages={'required': 'password is required', 'blank': 'password is required'})

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        qs = Login.objects.filter(email=email)
        qs1=Login.objects.filter(password=password)
        if qs.exists() and qs1.exists():
           return Response({'user':'login successfully'})
        return data


