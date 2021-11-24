from django.shortcuts import render , get_object_or_404 , redirect
from .models import *



def indexx(request):
	if request.method == 'POST':
		product = Products.objects.get(id=request.POST.get('id'))
		try:
			customer = request.user.customer
		except:
			device = request.COOKIES['device']
			customer, created = Customer.objects.get_or_create(device=device)

		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		orderItem, created = Items.objects.get_or_create(order=order, product=product)
		orderItem.save()
		items = Items.objects.filter(order = order)
		if items.count() == 0:
			A = 0
		else:
			A = 1
		total_price = 0
		for i in items:
			total_price += i.get_total
		context = {'order':order ,'ITEMS':items , 'totalprice':total_price ,'t':total_price + 35, 'A':A, 'Num_Items':order.get_total_item}
		return render(request, 'All/cart.html', context)
	if 'device' not in request.COOKIES:
		return render(request , 'All/index.html' , {'amour':Products.objects.filter(show_index=True), 'Num_Items':0})
	else:
		try: 
				customer = request.user.customer
		except:
			device = request.COOKIES['device']
			customer, created = Customer.objects.get_or_create(device=device)

		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		return render(request , 'All/index.html' , {'amour':Products.objects.filter(show_index=True), 'Num_Items':order.get_total_item})

def boutique(request):
	if request.method == 'POST':
		product = Products.objects.get(id=request.POST.get('id'))
		try:
			customer = request.user.customer
		except:
			device = request.COOKIES['device']
			customer, created = Customer.objects.get_or_create(device=device)

		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		orderItem, created = Items.objects.get_or_create(order=order, product=product)
		orderItem.save()
		items = Items.objects.filter(order = order)
		if items.count() == 0:
			A = 0
		else:
			A = 1
		total_price = 0
		for i in items:
			total_price += i.get_total
		context = {'order':order ,'ITEMS':items , 'totalprice':total_price ,'t':total_price + 35, 'A':A, 'Num_Items':order.get_total_item}
		return render(request, 'All/cart.html', context)
	else:
		if 'device' not in request.COOKIES:
			return render(request , 'All/boutique.html' , {'A':Products.objects.all(), 'Num_Items':0})
		else:
			try: 
					customer = request.user.customer
			except:
				device = request.COOKIES['device']
				customer, created = Customer.objects.get_or_create(device=device)

			order, created = Order.objects.get_or_create(customer=customer, complete=False)
			return render(request , 'All/boutique.html' , {'A':Products.objects.all(), 'Num_Items':order.get_total_item})

def amour(request):
	if request.method == 'POST':
		product = Products.objects.get(id=request.POST.get('id'))
		try:
			customer = request.user.customer
		except:
			device = request.COOKIES['device']
			customer, created = Customer.objects.get_or_create(device=device)

		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		orderItem, created = Items.objects.get_or_create(order=order, product=product)
		orderItem.save()
		items = Items.objects.filter(order = order)
		if items.count() == 0:
			A = 0
		else:
			A = 1
		total_price = 0
		for i in items:
			total_price += i.get_total
		context = {'order':order ,'ITEMS':items , 'totalprice':total_price ,'t':total_price + 35, 'A':A}
		return render(request, 'All/cart.html', context)
	else:
		if 'device' not in request.COOKIES:

			return render(request , 'All/amour.html' , {'A':Products.objects.filter(category='Amour'),
 		'B':Products.objects.filter(category='All'),
 		'C':Products.objects.filter(category='Amour_Anniv'),
 		'D':Products.objects.filter(category='Naiss_Amour'),
 		'E':Products.objects.filter(category='Amour_Naiss_Anniv'),
			'Num_Items':0
 		})
		else:
			try: 
					customer = request.user.customer
			except:
				device = request.COOKIES['device']
				customer, created = Customer.objects.get_or_create(device=device)

			order, created = Order.objects.get_or_create(customer=customer, complete=False)
			return render(request , 'All/amour.html' , {'A':Products.objects.filter(category='Amour'),
 		'B':Products.objects.filter(category='All'),
 		'C':Products.objects.filter(category='Amour_Anniv'),
 		'D':Products.objects.filter(category='Naiss_Amour'),
 		'E':Products.objects.filter(category='Amour_Naiss_Anniv'),
			'Num_Items':order.get_total_item,
 		})


def anniversaire(request):
	if request.method == 'POST':
			product = Products.objects.get(id=request.POST.get('id'))
			try:
				customer = request.user.customer
			except:
				device = request.COOKIES['device']
				customer, created = Customer.objects.get_or_create(device=device)

			order, created = Order.objects.get_or_create(customer=customer, complete=False)
			orderItem, created = Items.objects.get_or_create(order=order, product=product)
			orderItem.save()
			items = Items.objects.filter(order = order)
			if items.count() == 0:
				A = 0
			else:
				A = 1
			total_price = 0
			for i in items:
				total_price += i.get_total
			context = {'order':order ,'ITEMS':items , 'totalprice':total_price ,'t':total_price + 35, 'A':A}
			return render(request, 'All/cart.html', context)
	else:
		if 'device' not in request.COOKIES:
			return render(request , 'All/anniversaire.html' , {'A':Products.objects.filter(category='Anniv'),
 		'B':Products.objects.filter(category='Amour_Anniv'),
 		'C':Products.objects.filter(category='Anniv_Naiss_Reme'),
 		'D':Products.objects.filter(category='Amour_Naiss_Anniv'),
 		'E':Products.objects.filter(category='Anniv_Naiss'),
 		'F':Products.objects.filter(category='All'),
 		'G':Products.objects.filter(category='Anniv_Reme'),
			'Num_Items':0,
 		})
		else:
			try: 
					customer = request.user.customer
			except:
				device = request.COOKIES['device']
				customer, created = Customer.objects.get_or_create(device=device)

			order, created = Order.objects.get_or_create(customer=customer, complete=False)
			return render(request , 'All/anniversaire.html' , {'A':Products.objects.filter(category='Anniv'),
 		'B':Products.objects.filter(category='Amour_Anniv'),
 		'C':Products.objects.filter(category='Anniv_Naiss_Reme'),
 		'D':Products.objects.filter(category='Amour_Naiss_Anniv'),
 		'E':Products.objects.filter(category='Anniv_Naiss'),
 		'F':Products.objects.filter(category='All'),
 		'G':Products.objects.filter(category='Anniv_Reme'),
			'Num_Items':order.get_total_item,
 		})
 		

def naissance(request):
	if request.method == 'POST':
			product = Products.objects.get(id=request.POST.get('id'))
			try:
				customer = request.user.customer
			except:
				device = request.COOKIES['device']
				customer, created = Customer.objects.get_or_create(device=device)

			order, created = Order.objects.get_or_create(customer=customer, complete=False)
			orderItem, created = Items.objects.get_or_create(order=order, product=product)
			orderItem.save()
			items = Items.objects.filter(order = order)
			if items.count() == 0:
				A = 0
			else:
				A = 1
			total_price = 0
			for i in items:
				total_price += i.get_total
			context = {'order':order ,'ITEMS':items , 'totalprice':total_price ,'t':total_price + 35, 'A':A}
			return render(request, 'All/cart.html', context)
	else:
		if 'device' not in request.COOKIES:
			return render(request , 'All/naissance.html' , {'A':Products.objects.filter(category='Amour_Naiss_Anniv'),
 		'B':Products.objects.filter(category='Naiss_Amour'),
 		'C':Products.objects.filter(category='All'),
 		'D':Products.objects.filter(category='Naiss_Amour'),
 		'E':Products.objects.filter(category='Anniv_Naiss_Reme'),
 		'F':Products.objects.filter(category='Anniv_Naiss'),
			'Num_Items':0,
 		})
		else:
			try: 
					customer = request.user.customer
			except:
				device = request.COOKIES['device']
				customer, created = Customer.objects.get_or_create(device=device)

			order, created = Order.objects.get_or_create(customer=customer, complete=False)
			return render(request , 'All/naissance.html' , {'A':Products.objects.filter(category='Amour_Naiss_Anniv'),
 		'B':Products.objects.filter(category='Naiss_Amour'),
 		'C':Products.objects.filter(category='All'),
 		'D':Products.objects.filter(category='Naiss_Amour'),
 		'E':Products.objects.filter(category='Anniv_Naiss_Reme'),
 		'F':Products.objects.filter(category='Anniv_Naiss'),
			'Num_Items':order.get_total_item,
 		})
 	

def remerciement(request):
	if request.method == 'POST':
		product = Products.objects.get(id=request.POST.get('id'))
		try:
			customer = request.user.customer
		except:
			device = request.COOKIES['device']
			customer, created = Customer.objects.get_or_create(device=device)
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		orderItem, created = Items.objects.get_or_create(order=order, product=product)
		orderItem.save()
		items = Items.objects.filter(order = order)
		if items.count() == 0:
			A = 0
		else:
			A = 1
		total_price = 0
		for i in items:
			total_price += i.get_total
		context = {'order':order ,'ITEMS':items , 'totalprice':total_price ,'t':total_price + 35, 'A':A}
		return render(request, 'All/cart.html', context)
	else:
		if 'device' not in request.COOKIES:

			return render(request , 'All/remerciment.html' , {'A':Products.objects.filter(category='Reme'),
 		'B':Products.objects.filter(category='Anniv_Naiss_Reme'),
 		'C':Products.objects.filter(category='All'),
 		'D':Products.objects.filter(category='Anniv_Reme'),
			'Num_Items': 0,
 		})
		else:
			try: 
					customer = request.user.customer
			except:
				device = request.COOKIES['device']
				customer, created = Customer.objects.get_or_create(device=device)

			order, created = Order.objects.get_or_create(customer=customer, complete=False)
			return render(request , 'All/remerciement.html' , {'A':Products.objects.filter(category='Reme'),
 		'B':Products.objects.filter(category='Anniv_Naiss_Reme'),
 		'C':Products.objects.filter(category='All'),
 		'D':Products.objects.filter(category='Anniv_Reme'),
			'Num_Items': order.get_total_item,
 		})


def product(request, id_test):
	product = Products.objects.get(id=id_test)
	if(id_test >= 28):
		product = Products.objects.get(id=id_test)
		context = {
  'pro':product,
  'pro1' : get_object_or_404(Products , pk=int(id_test)-1),
  'pro2' : get_object_or_404(Products , pk=int(id_test)-2),
  'pro3' : get_object_or_404(Products , pk=int(id_test)-3),
  'pro4' : get_object_or_404(Products , pk=int(id_test)-4),
 }
	else:
		context = {'pro':product,
		'pro1' : get_object_or_404(Products , pk=int(id_test)+1),
 	'pro2' : get_object_or_404(Products , pk=int(id_test)+2),
 	'pro3' : get_object_or_404(Products , pk=int(id_test)+3),
 	'pro4' : get_object_or_404(Products , pk=int(id_test)+4)
		}
		#Get user account information
	if request.method == 'POST':
		try:
			customer = request.user.customer
		except:
			device = request.COOKIES['device']
			customer, created = Customer.objects.get_or_create(device=device)

		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		orderItem, created = Items.objects.get_or_create(order=order, product=product)
		orderItem.save()

		return redirect('cart')
	else:
		if 'device' not in request.COOKIES:
			context['Num_Items'] = 0
			return render(request, 'All/product.html', context)
		else:
			try:
				customer = request.user.customer
			except:
				device = request.COOKIES['device']
				customer, created = Customer.objects.get_or_create(device=device)

			order, created = Order.objects.get_or_create(customer=customer, complete=False)
			context['Num_Items'] = order.get_total_item
			return render(request , 'All/product.html' , context)
		


def cart(request):
	if request.COOKIES['device'] in Customer.objects.filter(device=str(request.COOKIES['device'])):
		if request.method =='POST':
			customer = request.user.customer
			proo = Products.objects.get(id = int(request.POST.get('id')))
			order, created = Order.objects.get_or_create(customer=customer, complete=False)
			record = Items.objects.get(product = proo , order = order)
			record.delete()
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = Items.objects.filter(order = order)
		if items.count() == 0:
			A = 0
		else:
			A = 1
		total_price = 0
		for i in items:
			total_price += i.get_total
		context = {'order':order,'ITEMS':items , 'totalprice':total_price , 't':total_price + 35, 'A':A, 'Num_Items':order.get_total_item}
		return render(request, 'All/cart.html', context)
	else:
		if request.method == 'POST':
			device = request.COOKIES['device']
			proo = Products.objects.get(id = int(request.POST.get('id')))
			customer, created = Customer.objects.get_or_create(device=device)
			order, created = Order.objects.get_or_create(customer=customer, complete=False)
			record = Items.objects.get(product = proo , order = order)
			record.delete()
		device = request.COOKIES['device']
		customer, created = Customer.objects.get_or_create(device=device)
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = Items.objects.filter(order = order)
		if items.count() == 0:
			A = 0
		else:
			A = 1
		total_price = 0
		for i in items:
			total_price += i.get_total
		context = {'order':order ,'ITEMS':items , 'totalprice':total_price ,'t':total_price + 35, 'A':A , 'Num_Items':order.get_total_item}
		return render(request, 'All/cart.html', context)


def about(request):
	if 'device' not in request.COOKIES:
		return render(request , 'All/Qui_Sommes_Nous.html' , {'Num_Items':0})
	else:
		try: 
			customer = request.user.customer
		except:
			device = request.COOKIES['device']
			customer, created = Customer.objects.get_or_create(device=device)

		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		return render(request , 'All/Qui_Sommes_Nous.html' , {'Num_Items':order.get_total_item})


def Contact_Us(request):
	if 'device' not in request.COOKIES:
		return render(request , 'All/Contacez_Nous.html' , {'Num_Items':0})
	else:
		try: 
			customer = request.user.customer
		except:
			device = request.COOKIES['device']
			customer, created = Customer.objects.get_or_create(device=device)

		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		if request.method == 'POST':
			new_message = Message(customer = customer , name = request.POST.get('name') , email = request.POST.get('email') , subject = request.POST.get('subject') , message = request.POST.get('message'))
			new_message.save()
		return render(request , 'All/Contactez_Nous.html' , {'Num_Items':order.get_total_item})

def error_404_view(request , exception):
	return redirect('index')