from django.contrib import admin
from django.urls import path, include
from .import views
from mysite.views import detail, like

urlpatterns = [
    path('', views.mainpage),
    path('company/', views.company),
    path('<int:content_id>/', detail, name='detail'),
    path('like/<int:content_id>/', like, name='likes'),
]
