from django.shortcuts import render
from django.http import JsonResponse

from .models import Product, Category
from .serializers import CategorySerializer, ProductSerializer

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

def products_list(request):
    products = Product.objects.all().values()
    return JsonResponse(list(products), safe=False)

def product_detail(request,id):
    p=Product.objects.get(id=id)
    return JsonResponse({
        "id":p.id,
        "name":p.name,
        "price":p.price,
        "description": p.description,
        "count": p.count,
        "is_active": p.is_active,
        "category": p.category.id
    })
def categories_list(request):
    categories=Category.objects.all().values()
    return JsonResponse(list(categories),safe=False)

def category_detail(request, id):
    try:
        c = Category.objects.get(id=id)
        return JsonResponse({
            "id": c.id,
            "name": c.name
        })
    except Category.DoesNotExist:
        return JsonResponse({"error": "not found"}, status=404)



def category_products(request, id):
    products = Product.objects.filter(category_id=id).values()
    return JsonResponse(list(products), safe=False)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    
    @action(detail=True,methods=['get'])
    def products(self,request,pk=None):
        category=self.get_object()
        products=Product.objects.filter(category=category)
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
