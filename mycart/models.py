
from django.db import models	
from django.utils import timezone
# Create your models here.
class Product(models.Model):
	GIFT_CHOICES = [
    ('babygift','BABYGIFT'),
    ('birthdaygift', 'BIRTHDAYGIFT'),
    ('accentsgift','ACCENTSGIFT'),
    ('cristamgift','CRISTAMGIFT'),
    ('toysgift','TOYSGIFT'),
    ('valentinegift','VALENTINEGIFT'),
    ('artificialgift','ARTIFICIALGIFT'),
    ('giftforher','GIFTFORHER'),
    ('giftforhim','GIFTFORHIM'),
]
	product_name = models.CharField(max_length=100,null=True)
	desc = models.CharField(max_length=1000,null=True)
	category = models.CharField(max_length=100, choices=GIFT_CHOICES,default='babygift')
	subcategory = models.CharField(max_length=100,null=True)
	price = models.IntegerField(null=True)
	Image = models.ImageField(upload_to="shop/images",null=True)
	pub_date = models.DateField()

	def __str__(self):
		return self.product_name




class Cart(models.Model):
	product_name = models.CharField(max_length=100,null=True)
	desc = models.CharField(max_length=1000,null=True)
	category = models.CharField(max_length=100,null=True)
	subcategory = models.CharField(max_length=100,null=True)
	price = models.IntegerField(null=True)
	usern = models.CharField(max_length=100,null=True)
	Image = models.ImageField(upload_to="shop/images",null=True)
	pub_date = models.DateField()



class Orders(models.Model):

	STATE_CHOICES = [
    ('up','UP'),
    ('delhi', 'DELHI'),
    ('mp','MP'),
    ('maharastra','MAHARATRA'),
    ('gujrat','GUJRAT'),
    ('rajasthan','RAJASTHAN'),
    ('punjab','PUNJAB')
    ]
	order_id =models.AutoField(primary_key=True)
	email=models.EmailField(max_length=50,default="")
	name=models.CharField(max_length=100,default="")
	address1=models.CharField(max_length=100,default="")
	address2=models.CharField(max_length=100,default="")
	city=models.CharField(max_length=100,default="")
	state=models.CharField(max_length=100,choices=STATE_CHOICES,default="up")
	zip_code=models.IntegerField(max_length=6,default="")
	product_details=models.CharField(max_length=100,default="")























