from django.urls import path
from base.views import category_views as views
urlpatterns = [
    path('', views.getCategoryList, name='category_list'),
    path('detail/<str:cpk>/', views.getCategory, name='category_detail'),
    path('update/<str:pk>', views.updateCategory, name='category-update'),
    path('<str:cpk>/', views.getCategoryProducts, name='category'),
]
