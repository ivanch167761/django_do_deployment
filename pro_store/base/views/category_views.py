from base.models import Category, Product
from base.serializers import CategoryListSerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser

@api_view(['GET'])
def getCategoryList(request):
    categoryList = Category.objects.all()
    serializer = CategoryListSerializer(categoryList, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCategory(request, cpk):
    category = None
    category = Category.objects.get(_id=cpk)
    serializer = CategoryListSerializer(category, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getCategoryProducts(request, cpk):
    wantedCategory = Category.objects.filter(_id=cpk)
    wantedCategoryData = CategoryListSerializer(wantedCategory[0], many=False).data
    wantedCategoryId = wantedCategoryData['_id']
    categoryProducts = Product.objects.filter(category=wantedCategoryId)
    serializer = ProductSerializer(categoryProducts, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteCategory(request, cpk):
    category = Category.objects.get(_id=cpk)
    category.delete()
    return Response('Category deleted')

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateCategory(request, pk):
    data = request.data
    category = Category.objects.get(_id=pk)
    category.category = data['category']
    category.description = data['description']
    category.save()
    serializer = CategoryListSerializer(category, many=False)
    return Response(serializer.data)
