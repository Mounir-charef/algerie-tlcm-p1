from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/dot', views.DotViewSet, basename='dot')
router.register('api/cmp', views.CmpViewSet, basename='cmp')

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.homePage, name="home"),
    path('chart/', views.homePage, name="chart"),
    path('api/region/', views.getCmpsName, name="cmps_name"),
    path('api/region/<str:pk>/', views.getCmpName, name="cmp_name"),
]
