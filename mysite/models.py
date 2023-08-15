from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pics/%y%m/%d/',  null=True)
    sub_content = models.CharField(max_length=200, default='', null=True)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    isMain = models.BooleanField()