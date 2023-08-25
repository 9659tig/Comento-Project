from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import  login_required
from .models import Product, Comment
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

@login_required(login_url='accounts:login')
def comment_update(req, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if req.user != comment.author:
        raise PermissionDenied

    if req.method == 'POST':
        form = CommentForm(req.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('detail', content_id=comment.content_list.id)
    else:
        form = CommentForm(instance=comment)

    context = {'comment': comment, 'form': form}
    return render(req, 'mysite/comment_form.html', context)

@login_required(login_url='accounts:login')
def comment_delete(req, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if req.user != comment.author:
        raise PermissionDenied
    else:
        comment.delete()
    return redirect('detail', content_id=comment.content_list.id)

@login_required(login_url='accounts:login')
def like(req, content_id):
    post = Product.objects.get(id=content_id)
    user = req.user
    if post.like.filter(id=req.user.id).exists():
        post.like.remove(user)
        return JsonResponse({'message': 'deleted', 'like_cnt' : post.like.count()})
    else:
        post.like.add(user)
        return JsonResponse({'message': 'added', 'like_cnt' : post.like.count()})

