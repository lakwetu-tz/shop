from django.db import models
from autoslug import AutoSlugField



class Category(models.Model):
    # parent = models.CharField(max_length=255)
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.CharField(max_length=50, blank=True, null=True) # use autoslug
    # logo = models.ImageField(upload_to='media/catlogo', blank=True, null=True, help_text='Optional')
    # logo1 = models.ImageField(upload_to='media/catlogo', blank=True, null=True, help_text='Optional')
    # logo2 = models.ImageField(upload_to='media/catlogo', blank=True, null=True, help_text='Optional')
    top_three_cat = models.BooleanField(default=False)
    more = models.BooleanField(default=False, blank=True, verbose_name="For Add In Right Menu")
    created_at = models.DateTimeField(null=True, blank=True)
    disc = models.BooleanField(default=False, verbose_name='Add In Disclaimer')
    hit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # image = models.ImageField()
    # image_alt_name = models.CharField(max_length=200, blank=True)
    price = models.IntegerField(null=True, blank=True)
    old_price = models.IntegerField(null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True)
    hit = models.PositiveIntegerField(default=0) 


class Cart(models.Model):
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Feature(models.Model):    
    title = models.CharField(max_length=500)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='feature_posts')
    content = models.CharField( max_length=50, blank=True, null=True)

class Comment(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    # user = models.ForeignKey(
    #     User, 
    #     on_delete=models.CASCADE, 
    #     related_name='comments'
    # )
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name) 