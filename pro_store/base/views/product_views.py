from base.models import Category, Product
from base.serializers import CategoryListSerializer, ProductSerializer
from rest_framework.decorators import api_view
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
