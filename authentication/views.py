from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(APIView):
    def post(self, request):
        serialize_data = RegisterSerializer(data=request.data)

        if serialize_data.is_valid():
            serialize_data.save()
            return Response({'message': 'User have registered successfully', 'data': serialize_data.validated_data}, status=status.HTTP_201_CREATED)

        return Response(serialize_data.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():

            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)
            if not user:
                return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)

            refresh = RefreshToken.for_user(user)
            tokens = {
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }

            return Response({'message': "User has successfully logined", 'tokens':tokens}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutVIew():
    pass

