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
        fields = "__all__"

class StockSerializer(serializers.ModelSerializer):
    # positions = ProductPositionSerializer(many=True)
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock

        fields = '__all__'

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
    '''в методе create() пройдитесь циклом по positions и создайте позиции склада for
     position in positions: StockProduct.objects.create(stock=..., product=..., price=..., quantity=...) '''

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')


        # создаем склад по его параметрам
        stock = super().create(validated_data)
        product = super().create(validated_data)
        price = super().create(validated_data)
        quantity = super().create(validated_data)

        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for position in positions:
            # StockProduct.objects.create(stock=stock, **position)
            StockProduct.objects.create(stock=stock, product=product, price=price, quantity=quantity)

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # обновляем склад по его параметрам / обращение к modelSerializer
        stock = super().update(instance, validated_data)
        product = super().create(validated_data)
        price = super().create(validated_data)
        quantity = super().create(validated_data)
        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for position in positions:
            object, created = StockProduct.objects.update_or_create(
                stock=stock,
                product=position['product'],
                defaults={'stock': stock, 'product': position['product'], 'quantity': position['quantity'],
                          'price': position['price']}
            )

        return stock
        # # достаем связанные данные для других таблиц
        # positions = validated_data.pop('positions')
        #
        # product = super().update(instance, validated_data)
        # price = super().update(instance, validated_data)
        # quantity = super().update(instance, validated_data)
        #
        # # обновляем склад по его параметрам
        # stock = super().update(instance, validated_data)
        # for position in positions:
        #     obj = StockProduct.objects.update_or_create(stock=stock, product=product,price=price,quantity=quantity
        #                                           defaults={'price':, 'quantity': ...})
        #
        #     defaults = {'first_name': 'Bob'}
        #     try:
        #         obj = Person.objects.get(first_name='John', last_name='Lennon')
        #         for key, value in defaults.items():
        #             setattr(obj, key, value)
        #         obj.save()
        #     except Person.DoesNotExist:
        #         new_values = {'first_name': 'John', 'last_name': 'Lennon'}
        #         new_values.update(defaults)
        #         obj = Person(**new_values)
        #         obj.save()
        #
        # # здесь вам надо обновить связанные таблицы
        # # в нашем случае: таблицу StockProduct
        # # с помощью списка positions
        #
        # return stock
    # _____________________________________________________________________________________________
    # Нашел пример как это сделано другими:
    # class TrackSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Track
    #         fields = ['order', 'title', 'duration']
    #
    # class AlbumSerializer(serializers.ModelSerializer):
    #     tracks = TrackSerializer(many=True)
    #
    #     class Meta:
    #         model = Album
    #         fields = ['album_name', 'artist', 'tracks']
    #
    #     def create(self, validated_data):
    #         tracks_data = validated_data.pop('tracks')
    #         album = Album.objects.create(**validated_data)
    #         for track_data in tracks_data:
    #             Track.objects.create(album=album, **track_data)
    #         return album
    # _______________________________________________________________________________

    # def create(self, validated_data):
    #     positions = validated_data.pop('positions')
    #     stock = super().create(**validated_data)
    #     product = Stock.create(**validated_data)
    #     price = Stock.create(**validated_data)
    #     quantity = Stock.create(**validated_data)
    #     for position in positions:
    #         StockProduct.objects.create(stock_id=stock,product=product,price=price,quantity=quantity, **position)
    #     return stock
    # def create(self, validated_data):
    #     positions = validated_data.pop('positions')
    #     stock = super().create(validated_data)
    #     # stock = Stock.objects.create(validated_data)
    #     # product = Stock.objects.create(validated_data)
    #     # price = Stock.objects.create(validated_data)
    #     # quantity = Stock.objects.create(validated_data)
    #     for position in positions:
    #         StockProduct.objects.create(stock=stock,product=product,price=price,quantity=quantity, **position)
    #     return stock


    # def update(self, instance, validated_data):
    #     positions = validated_data.pop('positions')
    #     positions.save()
    #     return instance
    #     # обновляем склад по его параметрам
    #     stock = super().update(instance, **validated_data)
    #     for position in positions:
    #         field, value = StockProduct.objects.update_or_create(**position)
    #         StockProduct.object.create(position=field, stock=value)
    #         return stock


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
            #     for position in positions:
            #         StockProduct.objects.create(stock=stock, **position)
            #
            #     return stock
            # StockProduct.objects.create(stock=position.stock,
            #                             product =position.product,
            #                             price=position.price,
            #                             quantity=position.quantity)
    #
    #
    #         stock = super().create(**positions)
    #         return stock
        # return stock
        #

        # return validated_data
        # заполняю stockproduct

    #     print(positions)

        # создаем склад по его параметрам
        # stock = super().create(**validated_data)# переопределение поведения родительского класса create
        # for position in positions:
        #     print(position)
        #     field, value = StockProduct.objects.update_or_create(**position)
        #     StockProduct.object.create(position = field,stock= value)
        #     return stock

    # def update(self, instance, validated_data):
    # #     # достаем связанные данные для других таблиц
    #     positions = validated_data.pop('positions')
    #     positions.save()
    #
    #     return instance
    #
    #     # обновляем склад по его параметрам
    #     stock = super().update(instance, **validated_data)
    #     for position in positions:
    #         print(position)
    #         field, value = StockProduct.objects.update_or_create(**position)
    #         StockProduct.object.create(position=field, stock=value)
    #         return stock



        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

# _____________________________________________________________________________________________________


# def create(self, validated_data):
#     # достаем связанные данные для других таблиц
#     if 'positions' not in self.initial_data:
#         positions = Stock.objects.create(**validated_data)
#     positions = validated_data.pop('positions')
#     else:
#
#     stock = super().create(**validated_data)  # переопределение поведения родительского класса create
#     for position in positions:
#         print(position)
#         # тут начинается непонятное:
#         # непонятно как посмотреть те данные которые приходят в positions. Что нужно сделать, чтобы print(positions)что-то отобразил?
#         делаю такой запрос: {
#                 "id": 1,
#                 "positions": [
#                     {
#                         "id": 1,
#                         "product": {
#                             "id": 1,
#                             "title": "Notebook",
#                             "description": "Goog one"
#                         },
#                         "quantity": 1,
#                         "price": "10000.00",
#                         "stock": 1
#                     }
#                 ],
#                 "address": "Shelkovskaya",
#                 "products": [
#                     1
#                 ]
#             }
#         # post ->  "product with this title already exists."
#         # print() при этом ничего не выводит. То есть даже тип данных не могу посмотреть.
#
#         field, value = StockProduct.objects.update_or_create(**position)
#         StockProduct.object.create(position=field, stock=value)
#         return stock

# # пробовал через vs code , там ошибки.
# POST http://127.0.0.1:8000/api/v1/stocks/
# Content-Type: application/json
#
#  {
#         "id": 4,
#         "positions": [],
#         "address": "Пятихатки -7",
#         "products": [3]
#     }

# ___________________________________________________________________________________


    # https: // mob25.com / serializatory - dlya - svyazannyh - modelej /  # %D0%A2%D0%B8%D0%BF_%D0%BF%D0%BE%D0%BB%D1%8F_StringRelatedField

    #

# class ProductSerializer(serializers.ModelSerializer):
#
#     # настройте сериализатор для продукта
#     class Meta:
#         model = Product
#         fields = "__all__"
#
# class ProductPositionSerializer(serializers.ModelSerializer):
#
#     product = ProductSerializer(read_only=True)
#
#     class Meta:
#         model = StockProduct
#         fields = "__all__"
#
# class StockSerializer(serializers.ModelSerializer):
#     positions = ProductPositionSerializer(many=True)
#     # # positions = ProductPositionSerializer(many=True)
#     # product = ProductSerializer(many=True)
#     class Meta:
#         model = Stock
#         fields = "__all__"

# ______________________________________________________________________________________________________________________


# class ProductSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Product
#         fields = '__all__'
# class StockSerializer(serializers.ModelSerializer):
#     product = ProductSerializer(read_only=True)
#     class Meta:
#         model = Stock
#         fields = "__all__"


# class ProductPositionSerializer(serializers.ModelSerializer):
#     # stock = StockSerializer(read_only=True)
#     product = ProductSerializer(read_only=True)
#
# def create(self, validated_data):
#     validated_data["stock"] = Stock.objects.create(**validated_data.pop("product"))
#     validated_data["product"] = Product.objects.create(**validated_data.pop("product"))
#     StockProduct.objects.create(**validated_data)
#     return validated_data
#
# # def update(self, instance, validated_data):
# #     instance
#
#     class Meta:
#         model = StockProduct
#         fields = "__all__"
# class StockSerializer(serializers.ModelSerializer):
#     positions = ProductPositionSerializer(many=True)
#     # # positions = ProductPositionSerializer(many=True)
#     # product = ProductSerializer(many=True)
#     class Meta:
#         model = Stock
#         fields = "__all__"

    #
    # def create(self, validated_data):
    #     validated_data["stock"] = Stock.objects.create(**validated_data.pop("stock"))
    #     validated_data["product"] = Product.objects.create(**validated_data.pop("product"))
    #     StockProduct.objects.create(**validated_data)
    #     return validated_data
    #
    # def update(self, instance, validated_data):
    #     instance


# ___________________________________________________________________________________________________
# class ProductSerializer(serializers.ModelSerializer):

#     # настройте сериализатор для продукта
#     class Meta:
#         model = Product
#         fields = "__all__"
#
# class ProductPositionSerializer(serializers.ModelSerializer):
#
#     product = ProductSerializer(read_only=True)
#
#     class Meta:
#         model = StockProduct
#         fields = "__all__"
#
#
# class StockSerializer(serializers.ModelSerializer):
#     stock = ProductPositionSerializer(read_only=True)
#     product = ProductSerializer(read_only=True)
#
#     class Meta:
#         model = StockProduct
#         fields = ["quantity", "price", "stock", "product"]
#
#     def create(self, validated_data):
#         validated_data["stock"] = Stock.objects.create(**validated_data.pop("stock"))
#         validated_data["product"] = Product.objects.create(**validated_data.pop("product"))
#         StockProduct.objects.create(**validated_data)
#         return validated_data
#
#     def update(self, instance, validated_data):
#         instance
# class StockSerializer(serializers.ModelSerializer):
    # # positions = ProductPositionSerializer(many=True)
    #
    # class Meta:
    #     model = Stock
    #     fields = "__all__"
    #
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
    #
    # def update(self, instance, validated_data):
    #     # достаем связанные данные для других таблиц
    #     positions = validated_data.pop('positions')
    #     stock = super().update(instance, validated_data)
    #
    #     return stock

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