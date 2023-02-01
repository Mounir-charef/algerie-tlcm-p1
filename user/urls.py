from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('login/', views.loginPage, name="login"),
    # path('projects/new/', views.createProject, name="projects"),
    # path('project/<str:pk>/update/', views.updateProject, name="create-project"),5
    # path('project/<str:pk>/delete/', views.deleteProject, name="delete-project"),
]
