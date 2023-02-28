from os import stat
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.serializers import ProductSerializer, OrderSerializer
from rest_framework import status
from base.models import Order, OrderItem, Product, ShippingAddress


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrderItems(request):
    user=request.user
    data=request.data
    print(data)
    orderItems = data['orderItems']

    if OrderItem and len(orderItems) == 0:
        return Response({'detail': 'No OrderItems'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        #1)create order
        totalPrice = 0
        for i in orderItems:
            product = Product.objects.get(_id=i['product_ID'])
            totalPrice += product.price*i['qty']
        order=Order.objects.create(
                user=user,
                paymentMethod=data['paymentMethod'],
                taxPrice=float(data['taxPrice'])*float(totalPrice),
                shippingPrice=data['shippingPrice'],
                totalPrice=totalPrice
                )
        #2)create ShippingAddress
        shipping=ShippingAddress.objects.create(
                order=order,
                address=data['address'],
                city=data['city'],
                postalCode=data['postalcode'],
                country=data['country']
                )
        #3)create order and set order to order relationship 
        for i in orderItems:
            product = Product.objects.get(_id=i['product_ID'])
            item = OrderItem.objects.create(
                    product=product,
                    order=order,
                    name=product.name,
                    qty=i['qty'],
                    price=product.price,
                    image=product.image.url
                    )
            #4)update stock
            product.countInStock -= item.qty
            product.save()
        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrderById(request, pk):
    user = request.user

    try:
        order = Order.objects.get(_id=pk)
        if user.is_staff or order.user == user:
            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data)
        else:
            Response({'detail': 'Not authorized to view this order'},
                    status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'detail': 'Order does not exists'}, status=status.HTTP_400_BAD_REQUEST)
