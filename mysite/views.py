from django.shortcuts import get_object_or_404, render
from .models import Product

def index(req):
    content_list = Product.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(req, 'mysite/content_list.html', context)

def products(req):
    content_list = Product.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(req, 'mysite/products_info.html', context)

def detail(req, content_id):
    MainContent = Product.objects
    content_list = get_object_or_404(MainContent, pk=content_id)
    context = {'content_list': content_list}
    return render(req, 'mysite/content_detail.html', context)