from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=20, null=True, black=True)
    # last_name = models.CharField(max_length=20, null=True, black=True)
    email = models.EmailField()
    mobile = models.CharField(max_length=20,null=False)
    Country = models.CharField(max_length=20,null=False, blank=True)
    Company = models.CharField(max_length=20,null=False, blank=True)
    Division =  models.CharField(max_length=20,null=False, blank=True)
    Zip_Code =  models.IntegerField(blank=True, default="1")
    Telephone =  models.IntegerField(blank=True, default="1")

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name
    
    @property
    def get_id(self):
        return self.user.id
    
    def __str__(self):
        return self.user.first_name


class Category(models.Model):
    # parent = models.CharField(max_length=255)
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.CharField(max_length=50, blank=True, null=True) # use autoslug
    logo = models.ImageField(upload_to='media/catlogo', blank=True, null=True, help_text='Optional')
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
    image = models.ImageField(upload_to='media/product')
    # image_alt_name = models.CharField(max_length=200, blank=True)
    price = models.IntegerField(null=True, blank=True)
    old_price = models.IntegerField(null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True)
    hit = models.PositiveIntegerField(default=0) 


class Cart(models.Model):
    cart_id = models.CharField(max_length=500, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    item = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='item')
    purchase = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.item}'
    
    def get_total(self):
        total = self.item.price
        float_total = format(total, '0.2f')
        return float_total

class Feature(models.Model):    
    title = models.CharField(max_length=500)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='feature_posts')
    content = models.CharField( max_length=50, blank=True, null=True)

class promocode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    # discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    amount = models.FloatField()
    active = models.BooleanField()

    def __str__(self):
        return self.code

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
    

class Order(models.Model):
    method = (
        ('DELIVERY', "DELIVERY"),
        ('PICK UP', "PICK UP")
    )
    orderitems = models.ManyToManyField(Cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    phone = models.CharField(max_length=10, null = False, default='0')
    coupon = models.ForeignKey(promocode, on_delete=models.SET_NULL, blank=True, null=True)
    total = models.DecimalField(max_digits=10, default=0, decimal_places=2, verbose_name='INR ORDER TOTAL')
    emailAddress = models.EmailField(max_length=250, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    payment_id = models.CharField(max_length=100, null=True)
    order_id =  models.CharField(max_length=100, null=True)

    def get_totals(self):
        total = 0
        for order_item in self.orderitems.all():
            total += float(order_item.get_total())
        if self.coupon:
            total -= self.coupon.amount
        return total
    
class Reviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

class clients(models.Model):    
    image= models.ImageField(upload_to='media/clients',null=True,blank=True)

class offers(models.Model):
    off = models.CharField(max_length=100, verbose_name='Total Off') 
    title = models.CharField(max_length=100, verbose_name='Title') 
    subtitle = models.CharField(max_length=100, verbose_name='Sub Title') 
    price = models.CharField(max_length=100, verbose_name='Price') 
    desc = models.CharField(max_length=100, verbose_name='Description') 
    button_text = models.CharField(max_length=100, verbose_name='Button Text') 
    button_url = models.URLField(max_length=500, default='', verbose_name='Button Link')
    small_desc = models.CharField(max_length=100, verbose_name='Small Description')
    active = models.BooleanField(default=False, verbose_name="Status")

    def __str__(self):
        return self.title 