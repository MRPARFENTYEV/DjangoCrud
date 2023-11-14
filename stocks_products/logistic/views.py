from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from django.http import Http404
from rest_framework.response import Response
from logistic.models import Product, Stock, StockProduct
from logistic.serializers import ProductSerializer, ProductPositionSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
# class ProductViewSet(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # def list(self, request):
    #     try:
    #         products = self.queryset
    #         serializer = self.serializer_class(products, many=True)
    #         return Response(serializer.data)
    #     except Http404:
    #         return Response({'message': 'Not found'}, status=404)
    # def retrieve(self, request):
    #     product = self.get_object()
    #     serializer = self.get_serializer(product)
    #     return Response(serializer.data)
    # # при необходимости добавьте параметры фильтрации
    #
    #
    # def destroy(self, request, pk=None):
    #     try:
    #         product = self.get_object()
    #         product.delete()
    #         return Response('Product deleted successfully.')
    #     except Product.DoesNotExist:
    #         return Response("Product doesn't exist.")
    #
    #
    # def update(self, request, pk):
    #     product = self.get_object()
    #     data = request.data
    #     if data:
    #         serializer = self.get_serializer(instance=product, data=data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response('No data provided.')

    #
    # def create(self, request):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response(serializer.data)

#
class StockViewSet(ModelViewSet):
# class StockViewSet(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
