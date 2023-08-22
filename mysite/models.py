from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pics/%y%m/%d/',  null=True)
    sub_content = models.CharField(max_length=200, default='', null=True)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    isMain = models.BooleanField()

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_list = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)