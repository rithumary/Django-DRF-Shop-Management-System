
from rest_framework import serializers
from .models import CategoryDb, ProductDb


class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryDb
        fields = "__all__"


class Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDb
        fields = "__all__"
