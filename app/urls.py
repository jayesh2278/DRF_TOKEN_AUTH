from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterAPI,LoginAPI,Bookview
from knox import views as knox_views
from rest_framework.routers import DefaultRouter
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/books', Bookview,basename="snippet")


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('', include(router.urls)),
]
