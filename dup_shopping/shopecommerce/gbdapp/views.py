from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from .models import category, product


# Create your views here.
def AllProdCat(request, c_slug=None):
    c_page = None
    products_list = None
    if c_slug != None:
        c_page = get_object_or_404(category, slug=c_slug)
        products_list = product.objects.all().filter(category=c_page, availability=True)
    else:
        products_list = product.objects.all().filter(availability=True)
    paginator = Paginator(products_list, 6)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, "category.html", {'category': c_page, 'products': products})


def AllProdetails(request, c_slug, product_slug):
    try:
        Product = product.objects.get(category__slug=c_slug, slug=product_slug)

    except Exception as e:
        raise e
    return render(request, 'product.html', {'Product': Product})
from django.shortcuts import render

# Create your views here.