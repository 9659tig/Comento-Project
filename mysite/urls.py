from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('products/', views.products),
    path('<int:content_id>/', views.detail, name='detail'),
    path('comment/create/<int:content_id>/', views.comment_create, name='comment_create'),
]
