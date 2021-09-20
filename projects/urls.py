from . import views
from django.urls import path ,include

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<int:project_id>/', views.detail, name='detail'),
]
               