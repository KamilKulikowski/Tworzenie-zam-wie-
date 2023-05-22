from django.shortcuts import render
from django import forms
from .models import Item, Order
from customers.models import User


class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"


from django.http import HttpResponse
from django.shortcuts import render


def item_create(request):
    if request.method == "POST":
        form = ItemCreateForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = ItemCreateForm()
    return render(request, "items/item_create.html", {"form": form})


def items_table(request):
    items = Item.objects.all()
    return render(request, "items/items_table.html", {"items": items})


from django.http import JsonResponse
from django.shortcuts import render

from .models import Item


def items_table(request):
    items = Item.objects.all()
    context = {
        "items": items,
    }

    return render(request, "items/items_table.html", context=context)


def add_to_cart(request, item_id):
    cart_in_session = request.session["cart"] if "cart" in request.session else []
    cart_in_session.append(item_id)
    request.session.update({"cart": cart_in_session})
    return JsonResponse({"message": "Added item to cart."})


def cart(request):
    context = {}
    cart = {}
    summary = 0
    if "cart" in request.session:
        for item_id in request.session["cart"]:
            price = Item.objects.get(id=item_id).price
            cart[item_id] = [
                Item.objects.get(id=item_id),
                request.session["cart"].count(item_id),
                int(price) * request.session["cart"].count(item_id),
            ]
            summary += int(price)
    print(cart)
    context["items"] = cart
    context["summary"] = summary
    request.session.update({"summary": summary})
    return render(request, "items/cart.html", context=context)


def clear_cart(request):
    request.session.update({"cart": []})
    del request.session["cart"]
    return JsonResponse({"message": "Cart has been cleared."})


def place_order(request):
    if "cart" in request.session:
        order = Order.objects.create()
        order.products = request.session["cart"]
        user = request.user
        order.customer = user.id
        order.price = request.session["summary"]
        order.save()
        return JsonResponse({"message": "Order placed! Your new order number: "+ str(order.id)})
    else:
        return JsonResponse({"message": "Cart can't be empty!"})


def orders(request):
    user = request.user
    user_id = user.id
    orders = Order.objects.filter(customer=user_id)
    context = {
        "orders": orders,
    }
    return render(request, "items/orders.html", context=context)


def order_details(request, order_id):
    order_items = {}
    try:
        order_info = Order.objects.get(pk=order_id)
        order_products = order_info.products.strip('][').split(', ')
        for item_id in order_products:
            price = Item.objects.get(id=item_id).price
            order_items[item_id] = [
                Item.objects.get(id=item_id),
                order_products.count(item_id),
                int(price) * order_info.products.count(item_id),
            ]
    except Order.DoesNotExist as e:
        print(e)
        order_info = Order.objects.none()


    context = {
        "info": order_info,
        "products": order_items,
    }

    return render(request, "items/order_details.html", context=context)
