from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models import Category,Product,RelatedImage
from django.db.models import Q
# Create your views here.

def homepage(request):
    products = Product.objects.all()
    context = {
        "products":products
    }
    return render(request,'index.html',context)

def product_details(request,slug):

    product_info = Product.objects.get(slug=slug)
    related_product = Product.objects.filter(category=product_info.category).exclude(id=product_info.id)[0:4]
    related_image = RelatedImage.objects.filter(product=product_info)

    context = {
        "product_info":product_info,
        "related_product":related_product,
        "related_image":related_image,
    }
    return render(request,'store/products.html',context)

def category_filtering(request,id):
    cat_obj = Category.objects.get(id=id)
    products = Product.objects.filter(category__id=cat_obj.id)
    context = {
        'products':products
    }
    return render(request,'store/filter.html',context)

def product_search(request):
    search_data = request.GET.get('search')
    search_product = Product.objects.filter(Q(name__icontains = search_data) | Q(desc__icontains = search_data))

    context = {
        "search_product":search_product
    }
    return render(request,'store/search.html',context)


