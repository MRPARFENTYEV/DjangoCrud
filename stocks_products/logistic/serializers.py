from rest_framework import serializers
from django.db import models

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):

    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = "__all__"




class ProductPositionSerializer(serializers.ModelSerializer):

    product = ProductSerializer(read_only=True)

    class Meta:
        model = StockProduct
        fields = "__all__"

class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    # # positions = ProductPositionSerializer(many=True)
    # product = ProductSerializer(many=True)
    class Meta:
        model = Stock
        fields = "__all__"


    #
    # def create(self, validated_data):
    #     validated_data["stock"] = Stock.objects.create(**validated_data.pop("stock"))
    #     validated_data["product"] = Product.objects.create(**validated_data.pop("product"))
    #     StockProduct.objects.create(**validated_data)
    #     return validated_data
    #     def create(self, validated_data):
    #         product_data = validated_data.pop('positions')
    #         stock_data = (
    #             super().create(validated_data))
    #         # Создание продукта
    #         product = models.Product.objects.create(**product_data)
    #         # stock = models.Stock.objects.create(product=product, **stock_data)
    #         return stock_data
    # def update(self, instance, validated_data):
    #     instance

#     def create(self, validated_data):
#         product_data = validated_data.pop('positions')
#         stock_data = super().create(validated_data)
#         # Создание продукта
#         product = models.Product.objects.create(**product_data)
#         # stock = models.Stock.objects.create(product=product, **stock_data)
#         return stock_data
# def create(self, validated_data):
#     stock_product_data = validated_data.pop('stock_product')
#     stock_product = StockProduct.objects.create(**stock_product_data)
#     validated_data['stock_product'] = stock_product.id
#     return Logistic.objects.create(**validated_data)

# def create(self, validated_data):
#     # достаем связанные данные для других таблиц
#     positions = validated_data.pop('positions')
#
#     # создаем склад по его параметрам
#     stock = super().create(validated_data)
#
#     # здесь вам надо заполнить связанные таблицы
#     # в нашем случае: таблицу StockProduct
#     # с помощью списка positions
#
#     return stock

  # def create(self, validated_data):
  #       # validated_data - это данные, прошедшие проверку
  #       # сериализатора, они могут быть изменены
  #
  #       product = Product.objects.create(**validated_data)
  #       return product