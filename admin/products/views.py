from django.http import response
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from products.serializers import ProductSerializer
from products.models import Product,User
from products.producer import publish
import random
# Create your views here.
class ProductViewSet(viewsets.ViewSet):
    
    def list(self, request): # /api/products
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_created',serializer.data)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
        pass

    def retrieve(self, request, pk=None): # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
        pass

    def update(self, request, pk=None): # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_upated',serializer.data)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

    def destory(self, request, pk=None): # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        product.delete()
        publish('product_delete',pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
          'id': user.id
        })
