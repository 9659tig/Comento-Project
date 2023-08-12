from django.shortcuts import render
from .models import Product

def index(req):
    content_list = Product.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(req, 'mysite/content_list.html', context)
