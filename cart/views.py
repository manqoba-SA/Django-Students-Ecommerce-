from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from GetItApp.models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,quantity=cd['quantity'],override_quantity=cd['override'])
    return redirect('cart:cart_table')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_table')

def cart_table(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    cart = Cart(request)
    for item in cart:
    	item['update_quantity_form'] = CartAddProductForm(initial={
		'quantity': item['quantity'],
		'override': True,})
    context = {'cart': cart, 'category': category, 'categories': categories}
    return render(request, 'carttable.html', context)

