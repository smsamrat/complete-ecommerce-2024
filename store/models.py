from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    mainimage = models.ImageField(upload_to='category_image',blank=True,null=True)
    slug = models.SlugField(max_length=200,blank=True,null=True)
    parent =  models.ForeignKey('self',on_delete=models.CASCADE,related_name="child_category",blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="category")
    mainimage = models.ImageField(upload_to='prouct_image')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True,blank=True,null=True)
    desc = models.TextField()
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)
    stock = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        else:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class RelatedImage(models.Model):
    image = models.ImageField(upload_to='related_product_image')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="related_product_image")



