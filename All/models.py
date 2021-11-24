from django.core.checks import messages
from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True, blank=True)
	email = models.CharField(max_length=200, null=True, blank=True)
	device = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		if self.name:
			name = self.name
		else:
			name = self.device
		return str(name)


class Products(models.Model):
    x=[
        ('All','All'),('Amour_Anniv','Amour_Anniv'),
        ('Naiss_Amour','Naiss_Amour'),('Reme','Reme'),
        ('Amour','Amour'),('Anniv_Naiss_Reme','Anniv_Naiss_Reme'),
        ('Amour_Naiss_Anniv','Amour_Naiss_Anniv'),('Anniv_Naiss','Anniv_Naiss'),
        ('Anniv','Anniv'),('Anniv_Reme','Anniv_Reme'),
    ]
    img = models.ImageField(upload_to='photos/%y/%m/%d')
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=20,choices=x)
    show_index = models.BooleanField(default=False)

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_total_item(self):
		items = Items.objects.filter(order = self)
		it = 0
		for item in items:
			it += 1
		return it



class Items(models.Model):
	product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price
		return total



class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address


class Message(models.Model):
	customer = models.ForeignKey(Customer , on_delete=models.SET_NULL , null=True)
	name = models.CharField(max_length=200 , null=False)
	email = models.CharField(max_length=200 , null=False)
	subject = models.CharField(max_length=100 , null=True)
	message = models.TextField(max_length=500 , null=False)