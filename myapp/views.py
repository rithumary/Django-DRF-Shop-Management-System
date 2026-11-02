from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CategoryDb, ProductDb
from .serializers import Category_Serializer, Product_Serializer

# Create your views here.

class Category_API(APIView):

    def get(self, request):
        category = CategoryDb.objects.all()
        serializer = Category_Serializer(category, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Category_Serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Category_Detail_API(APIView):

    def get(self, request, pk):
        category = CategoryDb.objects.get(id=pk)
        serializer = Category_Serializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = CategoryDb.objects.get(id=pk)
        serializer = Category_Serializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = CategoryDb.objects.get(id=pk)
        category.delete()
        return Response({"message": "Category Deleted Successfully"})


class Product_API(APIView):

    def get(self, request):
        product = ProductDb.objects.all()
        serializer = Product_Serializer(product, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Product_Serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Product_Detail_API(APIView):

    def get(self, request, pk):
        product = ProductDb.objects.get(id=pk)
        serializer = Product_Serializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = ProductDb.objects.get(id=pk)
        serializer = Product_Serializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = ProductDb.objects.get(id=pk)
        product.delete()
        return Response({"message": "Product Deleted Successfully"})

