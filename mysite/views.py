from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import  login_required
from .models import Product
from .forms import CommentForm

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

@login_required(login_url='accounts:login')
def comment_create(req, content_id):
    content_list = get_object_or_404(Product, pk=content_id)

    if req.method == 'POST':
        form = CommentForm(req.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_list = content_list
            comment.author = req.user
            comment.save()
            return redirect('detail', content_id=content_list.id)
        else:
            form = CommentForm()
            context = {'content_list':content_list, 'form':form}
            return render(req, 'mysite/content_detail.html', context)