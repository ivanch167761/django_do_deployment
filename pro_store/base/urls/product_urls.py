from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from base.views import product_views as views
urlpatterns = [
    path('', views.getProducts, name='products'),
    path('create/', views.createProduct, name='product-create'),
    path('upload/', views.uploadImage, name='image-upload'),
    path('uploadSecond/', views.uploadSecondImage, name='image-upload-second'),
    path('uploadThird/', views.uploadThirdImage, name='image-upload-third'),
    path('update/<str:pk>', views.updateProduct, name='product-update'),
    path('delete/<str:pk>/', views.deleteProduct, name='product-delete'),
    path('<str:pk>/', views.getProduct, name='product'),
]
