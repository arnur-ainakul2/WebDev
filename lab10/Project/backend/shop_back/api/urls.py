from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views.generics import (
    ProductListAPIView,
    ProductDetailAPIView,
    CategoryListAPIView,
    CategoryDetailAPIView,
    CategoryProductsAPIView
)
from api.views.cbv import ProductListAPIView, ProductDetailAPIView
from api.views import mixins as mixins_views
from api.views import CategoryViewSet, ProductViewSet


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)


urlpatterns = [
    # 🔹 CBV
    path('cbv/products/', ProductListAPIView.as_view()),
    path('cbv/products/<int:product_id>/', ProductDetailAPIView.as_view()),

    # 🔹 Mixins
    path('mixins/products/', mixins_views.ProductListAPIView.as_view()),
    path('mixins/products/<int:product_id>/', mixins_views.ProductDetailAPIView.as_view()),
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:product_id>/', ProductDetailAPIView.as_view()),

    # Categories
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:category_id>/', CategoryDetailAPIView.as_view()),

    # Custom
    path('categories/<int:category_id>/products/', CategoryProductsAPIView.as_view()),

]
