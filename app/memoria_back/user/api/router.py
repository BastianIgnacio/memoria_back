from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.api.views import UserApiView, UserApiView_Detail

urlpatterns = [
    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/users', UserApiView.as_view()),
    path('auth/users/<int:pk>/', UserApiView_Detail.as_view()),
]
