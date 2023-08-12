from django.shortcuts import render

def mainpage(req):
    return render(req, 'pages/mainpage.html')

def company(req):
    return render(req, 'pages/company_info.html')