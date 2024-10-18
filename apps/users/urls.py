from django.urls import path
from .views import RegisterView, UserListView, UserDetailView, CustomTokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user-detail'),
    # Ruta para obtener el token JWT
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
