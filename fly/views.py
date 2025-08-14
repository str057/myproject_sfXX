from django.shortcuts import render, get_object_or_404
from .models import Product


def index(request):
    products = Product.objects.all()
    print(f"Получено продуктов: {products.count()}")  # Отладка
    for product in products:
        print(f"Продукт: {product.name}")  # Отладка
    context = {"products": products}
    return render(request, "prod_list.html", context)


def prod_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "prod_detail.html", context)
