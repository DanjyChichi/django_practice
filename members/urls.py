from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.member_detail_page),
    path('', views.index),
]