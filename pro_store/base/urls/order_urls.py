from django.urls import path
from base.views import order_view as views

urlpatterns = [

        path('adminorders/', views.getOrders, name='orders'),
        path('myorders/', views.getMyOrders, name='myorders'),
        path('add/', views.addOrderItems, name='orders-add'),
        path('<str:pk>/', views.getOrderById, name='user-order'),
        path('<str:pk>/pay/', views.udateOrderToPaid , name='pay'),
        path('<str:pk>/delivered/', views.udateOrderToDelivered , name='delivered'),
        path('<str:pk>/tracking/', views.udateOrderTrackingNumber , name='tracking'),
]

