from django.urls import path
from . import views
from fly.views import ProdListView, ProdDetailView, ProdCreateView, ProdUpdateView, ProdDeleteView

app_name = "fly"

urlpatterns = [
    path("", ProdListView.as_view(), name="product_list"),
    path("product/<int:pk>/", ProdDetailView.as_view(), name="product_detail"),
    path('product/create/', ProdCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProdUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProdDeleteView.as_view(), name='product_delete'),
]



#skypro 19.08