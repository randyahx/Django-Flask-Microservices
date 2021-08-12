from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
import random

from .models import Product, User
from .serializers import ProductSerializer
from .producer import publish


class ProductViewSet(viewsets.ViewSet):  # These 5 methods come with the viewset
    def list(self, request):  # /api/products [GET]
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def create(self, request):  # /api/products [POST]
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        ## RabbitMQ ##  
        publish('product_created', serializer.data)
        ##############
        return Response(serializer.data, status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):  # /api/product/<str:id> [GET]
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):  # /api/product/<str:id> [POST]
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        ## RabbitMQ ##  
        publish('product_updated', serializer.data)
        ##############
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):  # /api/product/<str:id> [DELETE]
        product = Product.objects.get(id=pk)
        product.delete()
        ## RabbitMQ ##  
        publish('product_deleted', pk)
        ##############
        return Response(status=status.HTTP_204_NO_CONTENT)

# To check which status to return, send the request to postman and it will show the status

class UserAPIView(APIView):
    def get(self, _):
        user = User.objects.all()
        user = random.choice(user)
        return Response({
            id: user.id
        })
