from rest_framework.permissions import IsAdminUser
from rest_framework.utils.representation import serializer_repr
from base.models import Category, Product
from base.serializers import CategoryListSerializer, ProductSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = None

    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)


@api_view(['GET'])
def getCategoryProducts(request, cpk):
    wantedCategory = Category.objects.filter(category=cpk)
    wantedCategoryData = CategoryListSerializer(wantedCategory, many=True).data
    wantedCategoryId = wantedCategoryData[0]['_id']

    categoryProducts = Product.objects.filter(category=wantedCategoryId)
    serializer = ProductSerializer(categoryProducts, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getCategoryList(request):
    categoryList = Category.objects.all()
    serializer = CategoryListSerializer(categoryList, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteProduct(request, pk):
    product = Product.objects.get(_id=pk)
    product.delete()
    return Response('Product deleted')

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createProduct(request):
    user = request.user

    product = Product.objects.create(
            user = user, 
            category = Category.objects.get(_id=1),
            name = 'Sample name',
            brand = 'Sample Brand',
            countInStock = 0,
            description = '',
            price = '0',
    )

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateProduct(request, pk):
    data = request.data
    product = Product.objects.get(_id=pk)
    product.brand = data['brand']
    product.price = data['price']
    product.countInStock = data['countInStock']
    product.category = data['category']
    product.description = data['description']
    product.name = data['name']
    product.save()
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def uploadImage(request):
    data = request.data
    product_id = data['product_id']
    product = Product.objects.get(_id=product_id)
    product.image = request.FILES.get('image')
    product.save()
    return Response('Image was uploaded')


