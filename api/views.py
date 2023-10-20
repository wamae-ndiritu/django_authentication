from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def login(request):
    return Response({})


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        # Create a new user and hash the password
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()

        # Generate access token using MyTokenObtainPairSerializer
        access_token = MyTokenObtainPairSerializer().get_token(user)

        # Generate refresh token using RefreshToken
        refresh_token = RefreshToken.for_user(user)

        # Return both tokens and user data with 201 Created status code
        return Response({
            'access': str(access_token.access_token),
            'refresh': str(refresh_token),
        }, status=status.HTTP_201_CREATED)

    # If the data is not valid, return errors with 400 Bad Request status code
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def testRoute(request):
    return Response({})
