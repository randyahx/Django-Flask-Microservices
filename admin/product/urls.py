from django.contrib import admin
from django.urls import path

from .views import ProductViewSet   

urlpatterns = [
    path('product', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),  
    path('product/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'post': 'update',
        'delete': 'destroy'
    })),     
]
