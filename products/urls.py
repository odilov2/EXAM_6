from django.urls import path

from products.views import ShopView, ShopDetailView, ProductListView, ContactView

urlpatterns = [
    path('shop/', ShopView.as_view(), name='shop'),
    path('shopdetail/', ShopDetailView.as_view(), name='shop-detail'),
    path('products_detail', ProductListView.as_view(), name='products-detail'),
    path('contact/', ContactView.as_view(), name='contact'),
]
