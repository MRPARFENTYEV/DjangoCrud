from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from django.http import Http404
from rest_framework.response import Response
from logistic.models import Product, Stock, StockProduct
from logistic.serializers import ProductSerializer, ProductPositionSerializer, StockSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import serializers
# from stocks_products.logistic import serializers


class ProductViewSet(ModelViewSet):#
# class ProductViewSet(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','description']

class StockViewSet(ModelViewSet):

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['products']
    #реализуйте фильтрацию складов по товару

