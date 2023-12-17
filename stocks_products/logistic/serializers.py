from rest_framework import serializers
from django.db import models

from logistic.models import Product, Stock, StockProduct

from rest_framework import serializers
# from .models import Stock, Product, StockProduct

class ProductSerializer(serializers.ModelSerializer):

    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = "__all__"

class ProductPositionSerializer(serializers.ModelSerializer):
#
    class Meta:
        model = StockProduct
        fields = ['quantity','price']

class StockSerializer(serializers.ModelSerializer):
    # positions = ProductPositionSerializer(many=True)
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock

        fields = '__all__'


    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')


        # создаем склад по его параметрам
        stock = super().create(validated_data)
        product = super().create(validated_data)
        price = super().create(validated_data)
        quantity = super().create(validated_data)

        for position in positions:

            StockProduct.objects.create(stock=stock, product=product, price=price, quantity=quantity)

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        for position in positions:
            object, created = StockProduct.objects.update_or_create(
                stock=stock,
                product=position['product'],
                defaults={'stock': stock, 'product': position['product'], 'quantity': position['quantity'],
                          'price': position['price']}
            )

        return stock

