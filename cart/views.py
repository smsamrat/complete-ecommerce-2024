from django.shortcuts import render,redirect
from store.models import Product
from cart.models import *
from django.contrib import messages
# Create your views here.


def add_to_cart(request,id):
    item = Product.objects.get(id=id)
    cart_item = Cart.objects.get_or_create(cart_product=item,user=request.user)
    order_item = Order.objects.filter(user=request.user,ordered=False)
    if order_item.exists():
        orders = order_item[0]
        if orders.order_product.filter(cart_product=item,purchased=False).exists():
            order_quantity = request.POST.get('quantity')
            cart_item[0].quantity += int(order_quantity)
            cart_item[0].save()
            messages.info(request,"Product Quantity update")

        else:
            orders.order_product.add(cart_item[0])
            messages.success(request,"Product Added")
    else:
        order = Order(user=request.user)
        order.save()
        order.order_product.add(cart_item[0])

        # first add to cart korle ,sekhane quantity baria dile add hoy na sei issue fixed kora holo
        order_quantity = request.POST.get('quantity')
        cart_item[0].quantity += int(order_quantity) - 1 
        cart_item[0].save()

        messages.success(request,"Product Added")
    return redirect("/")


def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user,purchased=False)
    orders = Order.objects.filter(user=request.user,ordered=False)
    if cart_items.exists() and orders.exists():
        order = orders[0]

        context = {
            "cart_items":cart_items,
            "order":order
        }
        return render(request,'cart/cart_view.html',context)
    else:
        return render(request,'cart/cart_view.html')

        

    

def increment_quantity(request,id):
    product = Product.objects.get(id=id)
    cart = Cart.objects.get(cart_product=product)

    if cart.quantity >= 1:
        cart.quantity += 1
        cart.save()


    return redirect('cart_view')
     

def decrement_quantity(request,id):
    product = Product.objects.get(id=id)
    cart = Cart.objects.get(cart_product=product)

    if cart.quantity >= 1:
        cart.quantity -= 1
        cart.save()
    return redirect('cart_view')

# def remove_quantity(request,id):
#     product = Product.objects.get(id=id)
#     cart = Cart.objects.get(cart_product=product)
#     order_qs = Order.objects.filter(user=request.user,ordered=False)
#     if order_qs.exists():
#         order = order_qs[0]
#         order.order_product.filter(cart_product=product)
#         order.order_product.remove(cart)
#         cart.delete()
#     return redirect('cart_view')

def remove_quantity(request,id):
    product = Product.objects.get(id=id)
    cart = Cart.objects.get(user=request.user,cart_product=product)
    order_qs = Order.objects.filter(user=request.user,order_product=cart)[0]
    order_qs.order_product.remove(cart)
    cart.delete()
    return redirect('cart_view')


