from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Category
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