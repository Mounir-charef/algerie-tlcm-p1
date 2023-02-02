from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homePage, name="home"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.loginPage, name="login"),
]
