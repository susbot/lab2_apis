from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Product, Manufacturer


class ProductDetailView(DetailView):
    model = Product
    template_name = "product/product_detail.html"


class ProductListView(ListView):
    model = Product
    template_name = "product/product_list.html"
