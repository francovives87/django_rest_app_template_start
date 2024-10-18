# users/views.py

from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

# Vista para registrar un usuario
class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

# Vista para listar todos los usuarios
class UserListView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

# Vista para obtener un usuario específico
class UserDetailView(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

# Vista personalizada para obtener el token JWT (opcional)
class CustomTokenObtainPairView(TokenObtainPairView):
    # Si necesitas modificar el comportamiento o la respuesta del token,
    # puedes personalizar el serializer aquí.
    pass
