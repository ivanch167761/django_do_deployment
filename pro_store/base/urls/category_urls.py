from django.urls import path
from base.views import category_views as views
urlpatterns = [
    path('<str:cpk>/', views.getCategoryProducts, name='category'),
    path('', views.getCategoryList, name='category_list'),
]
