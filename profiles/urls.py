from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles import views

base_router = DefaultRouter()
base_router.register(
    'profiles', views.UserProfileViewSet)

base_router.register('feeds', views.FeedViewSet)


urlpatterns = [
    path(r'', include(base_router.urls)),
    path('login', views.UserLoginAPIView.as_view())
]
