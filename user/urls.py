from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homePage, name="home"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.loginPage, name="login"),
    path('api/dots/', views.getDotInformations, name="dots_info"),
    path('api/dot/<str:pk>', views.getDotInformation, name="dot_info"),
    path('api/cmps/', views.getCmpInformations, name="cmps_info"),
    path('api/cmp/<str:pk>', views.getCmpInformation, name="cmp_info"),
]
