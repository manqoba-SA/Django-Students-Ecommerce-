from django.shortcuts import render, get_object_or_404
from .models import Ordered_item, ServiceOrder, SpecialOrder
from .forms import OrderForm
from cart.cart import Cart
from GetItApp .models import Product, Month_Special

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                Ordered_item.objects.create(order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity'],)
            #clearing the cart
            cart.clear()
            return render(request, 'order_created.html', {'order':order})
    else:
        form = OrderForm()
    return render(request, 'checkout.html', {'cart':cart, 'form': form})

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def order(request):
    if request.method == 'POST':
        name = request.POST.get("person-name", True)
        surname = request.POST.get("surname", True)
        room_number = request.POST.get("room-number", True)
        product_name = request.POST.get("productname", True)
        building =request.POST.get("building", True)
        number = request.POST.get('cell', True)

    
        order_info = ServiceOrder(name=name, building=building, ordered_product=product_name, room_number=room_number, surname=surname, number=number)
        order_info.save()
        context = {"info":order_info}
        return render(request, "order_for_service.html", context)
    else:
        return render(request, "order_for_service.html")


@csrf_exempt
def order_for_special(request):
    if request.method == 'POST':
        name = request.POST.get("person-name", True)
        surname = request.POST.get("surname", True)
        room_number = request.POST.get("room-number", True)
        product_name = request.POST.get("productname", True)
        building =request.POST.get("building", True)
        number = request.POST.get('cell', True)

    
        order_info = SpecialOrder(name=name, building=building, ordered_product=product_name, room_number=room_number, surname=surname, number=number)
        order_info.save()
        special = Month_Special.objects.all()
        context = {"info":order_info, "specials": special}
        return render(request, "order_for_special.html", context)
    else:
        return render(request, "order_for_special.html")

