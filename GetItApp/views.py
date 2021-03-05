from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from cart.forms import CartAddProductForm
from .models import *

# Create your views here.
def home(request, category_slug=None):
    category = None
    specials = Month_Special.objects.all()
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    context = {'category': category, 'categories': categories, 'products': products, 'specials':specials}
    return render(request, 'home.html', context)

def products(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    cart_product_form = CartAddProductForm()
    context = {'category': category, 'categories': categories, 'products': products, 'cart_product_form': cart_product_form}
    return render(request, 'products.html',context)

def product_single(request, id, slug,category_slug=None):
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {'category': category, 'categories': categories,'product': product, 'cart_product_form': cart_product_form}
    return render(request, 'single.html', context)


def search_page(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(name__icontains=query) | Q(price__icontains=query)

            results=  Product.objects.filter(lookups).distinct()
            cart_product_form = CartAddProductForm()

            context={'results': results,
                     'submitbutton': submitbutton,'category': category, 'categories': categories, 'cart_product_form': cart_product_form}

            return render(request, 'SearchResults.html', context)

        else:
            return render(request, 'SearchResults.html')

    else:
        return render(request, 'SearchResults.html')