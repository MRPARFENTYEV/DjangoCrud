from rest_framework import routers
import rest_framework.routers


from logistic.views import ProductViewSet, StockViewSet
router = routers.DefaultRouter()
# router = rest_framework.DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)


urlpatterns = router.urls
