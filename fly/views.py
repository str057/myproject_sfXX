from django.db.migrations import CreateModel
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product

class ProdListView(ListView):
    model = Product
    template_name = 'fly/product_list.html'  # Явное указание шаблона
    context_object_name = 'products'


class ProdDetailView(DetailView):
    model = Product
    template_name = 'fly/product_detail.html'
    context_object_name = 'product'
    paginate_by = 12

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter +=1
        self.object.save()
        return self.object



class ProdCreateView(CreateView):
    model = Product
    fields = ("name", "category", "price", "image")
    success_url = reverse_lazy('fly:product_list')

class ProdUpdateView(UpdateView):
    model = Product
    fields = ("name", "category", "price", "image")
    success_url = reverse_lazy('fly:product_list')

    def get_success_url(self):
        return reverse('fly:product_detail', args=[self.kwargs.get('pk')])

class ProdDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('fly:product_list')







    #app_name/<model_name>_<action>
    #fly/product_list.html

#def index(request):
#    products = Product.objects.all()
 #   print(f"Получено продуктов: {products.count()}")  # Отладка
 #   for product in products:
 #       print(f"Продукт: {product.name}")  # Отладка
 #   context = {"products": products}
 #   return render(request, "product_list.html", context)


# def prod_detail(request, pk):
#   product = get_object_or_404(Product, pk=pk)
#  context = {"product": product}
#  return render(request, "product_detail.html", context)
