from django.urls import path
from rest_framework import routers
from . import views

# app_name = 'user'

router = routers.DefaultRouter()
router.register('api/dot', views.DotViewSet, basename='dot')
router.register('api/cmp', views.CmpViewSet, basename='cmp')

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.homePage, name="home"),
    path('api/region/', views.getCmpsName, name="cmps_name"),
    path('api/region/<str:pk>/', views.getCmpName, name="cmp_name"),
] + router.urls
