from django.shortcuts import render
from mysite.models import Product

def mainpage(req):
    content_list = Product.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(req, 'pages/mainpage.html', context)

def company(req):
    return render(req, 'pages/company_info.html')