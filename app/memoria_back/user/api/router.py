from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.api.views import UserApiView, UserApiView_Detail, Login, Logout

urlpatterns = [
    path('auth/login', Login.as_view()),
    path('auth/logout', Logout.as_view()),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/users', UserApiView.as_view()),
    path('auth/users/<int:pk>/', UserApiView_Detail.as_view()),
]
