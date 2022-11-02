from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from base.views import product_views as views
urlpatterns = [
    path('', views.getProducts, name='products'),
    path('<str:pk>/', views.getProduct, name='product'),
]
