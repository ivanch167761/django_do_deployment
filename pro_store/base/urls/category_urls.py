from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from base.views import category_views as views
urlpatterns = [
    path('<str:cpk>/', views.getCategoryProducts, name='category'),
    path('', views.getCategoryList, name='category_list'),
]
