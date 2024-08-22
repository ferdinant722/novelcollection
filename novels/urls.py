from django.urls import path
from . import views

urlpatterns = [
    path('', views.novel_list, name='novel_list'),
    path('novel/<int:pk>/', views.novel_detail, name='novel_detail'),
    path('novel/new/', views.novel_create, name='novel_create'),
    path('novel/<int:pk>/edit/', views.novel_edit, name='novel_edit'),
    path('novel/<int:pk>/delete/', views.novel_delete, name='novel_delete'),
]
