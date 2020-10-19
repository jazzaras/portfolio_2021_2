from . import views
from django.urls import path ,include

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
               