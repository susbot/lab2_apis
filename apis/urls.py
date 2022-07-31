from django.urls import path
from .views import product_list, product_detail

urlpatterns = [
    path("products/", product_list, name="product/product_list"),
    path("products/<int:pk>/", product_detail, name="product/product_detail"),
]