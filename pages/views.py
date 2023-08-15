from django.shortcuts import render
from mysite.models import Product
from django.conf import settings

def mainpage(req):
    content_list = Product.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(req, 'pages/mainpage.html', context)

def company(req):
    context = {'KAKAO_MAP_API_KEY': settings.KAKAO_MAP_API_KEY}
    return render(req, 'pages/company_info.html', context)