from django.shortcuts import render,redirect
from . models import Product,Cart,Orders
from django.contrib.auth.models import User,auth
# Create your views here.
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.

usern=''
list=[]
def cart(request,id):
	Car=Cart.objects.all()
	count=Car.count()
	list.append(count)
	print(count)
	pr=Product.objects.get(pk=id)
	cart=Cart()
	cart.product_name=pr.product_name
	cart.desc=pr.desc
	cart.category=pr.category
	cart.subcategory=pr.subcategory
	cart.price=pr.price
	cart.Image=pr.Image
	cart.pub_date=pr.pub_date
	if request.user.is_authenticated:
		cart.usern=request.user.username
		cart.save()
		return redirect('index')

	return render(request,'cart.html')



def register(request):
	if request.method=="POST":
		first_name=request.POST['firstname']
		last_name=request.POST['lastname']
		username=request.POST['username']
		email=request.POST['email']
		password=request.POST['password']
		confirm_password=request.POST['confirmpassword']
		if password==confirm_password:
			if User.objects.filter(username=username).exists():
				messages.error(request,'Username Taken')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.error(request,'Email Taken')
				return redirect('register')
			else:
				user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
				user.save();
				messages.success(request,'Account Created Successfully')
				return redirect('login')
		else:
			messages.error(request,'Password & Confirm Password Are Not Matching')
			return redirect('register')
	else:
		return render(request,'register.html')
def login(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('index')
		else:
			messages.error(request,"Username or Password is Incorrect")
			return redirect('login')
	return render(request,'login.html')
def logout(request):
	auth.logout(request)
	return redirect('index')
def checkout(request):
	cart=Cart.objects.all()
	return render(request,'checkout.html',{"cart":cart})
def vieworder(request):
	return render(request,'vieworder.html')
def myaccount(request):
	if request.user.is_authenticated:
		username=request.user.username
		first_name=request.user.first_name
		last_name=request.user.last_name
		email=request.user.email
	return render(request,'myaccount.html',{'username':username,'first_name':first_name,'last_name':last_name,'email':email})
def delivery(request):
	return render(request,'delivery.html')

def change_password(request):
	if request.method=="POST":
		form=PasswordChangeForm(request.user,request.POST)
		if form.is_valid():
			user=form.save()
			update_session_auth_hash(request,user)
			messages.success(request,'Your password was Successfully changed')
			return redirect('login')
		else:
			messages.error(request,'Please correct the error below')
	else:
		form= PasswordChangeForm(request.user)
	return render(request,'change_password.html',{'form':form})



def index(request):
	products=Product.objects.all()
	car=Cart.objects.all()
	cart=car.count()
	print(cart)
	return render(request,'index.html',{'product':products,'li':cart})
def contact(request):
	car=Cart.objects.all()
	cart=car.count()
	return render(request,'contact.html',{'li':cart})
def newproducts(request):
	bab=Product.objects.all()
	car=Cart.objects.all()
	cart=car.count()
	list=[]
	l1=[]
	l2=[]
	l3=[]
	l4=[]
	l5=[]
	l6=[]
	l7=[]
	l8=[]
	l9=[]
	for i in bab:
		dic1={}
		dic2={}
		dic3={}
		dic4={}
		dic5={}
		dic6={}
		dic7={}
		dic8={}
		dic9={}
		if i.category=='babygift':
			dic1.update({'id':i.id,'name':i.product_name,'category':i.category,'price':i.price,'desc':i.desc,'image':i.Image})
			l1.append(dic1)
		elif i.category=='birthdaygift':
			dic2.update({'id':i.id,'name':i.product_name,'category':i.category,'price':i.price,'desc':i.desc,'image':i.Image})
			l2.append(dic2)
		elif i.category=='accentsgift':
			dic3.update({'id':i.id,'name':i.product_name,'category':i.category,'price':i.price,'desc':i.desc,'image':i.Image})
			l3.append(dic3)
		elif i.category=='cristamgift':
			dic4.update({'id':i.id,'name':i.product_name,'category':i.category,'price':i.price,'desc':i.desc,'image':i.Image})
			l4.append(dic4)
		elif i.category=='toysgift':
			dic5.update({'id':i.id,'name':i.product_name,'category':i.category,'price':i.price,'desc':i.desc,'image':i.Image})
			l5.append(dic5)
		elif i.category=='artificialgift':
			dic6.update({'id':i.id,'name':i.product_name,'category':i.category,'price':i.price,'desc':i.desc,'image':i.Image})
			l6.append(dic6)
		elif i.category=='valentinegift':
			dic7.update({'id':i.id,'name':i.product_name,'category':i.category,'price':i.price,'desc':i.desc,'image':i.Image})
			l7.append(dic7)
		elif i.category=='giftforher':
			dic8.update({'id':i.id,'name':i.product_name,'category':i.category,'price':i.price,'desc':i.desc,'image':i.Image})
			l8.append(dic8)
		elif i.category=='giftforhim':
			dic9.update({'id':i.id,'name':i.product_name,'category':i.category,'price':i.price,'desc':i.desc,'image':i.Image})
			l9.append(dic9)


	print(l1[-1],l2[-1],l3[-1],l4[-1],l5[-1],l6[-1],l7[-1],l8[-1],l9[-1])
	list.append(l1[-1])
	list.append(l2[-1])
	list.append(l3[-1])
	list.append(l4[-1])
	list.append(l5[-1])
	list.append(l6[-1])
	list.append(l7[-1])
	list.append(l8[-1])
	list.append(l9[-1])
	print(list)
	return render(request,'newproducts.html',{'baby':list,'li':cart})
'''def myaccount(request):
	return render(request,'myaccount.html')'''
def location(request):
	car=Cart.objects.all()
	cart=car.count()
	return render(request,'location.html',{'li':cart})
def faq(request):
	car=Cart.objects.all()
	cart=car.count()
	return render(request,'faq.html',{'li':cart})
def shoppingcart(request):
	car=Cart.objects.all()
	cart=car.count()
	cartt=Cart.objects.all()
	return render(request,'cartitems.html',{'cart':cartt,'li':cart})
	
def specialoffer(request):
	car=Cart.objects.all()
	cart=car.count()
	pro=Product.objects.all()
	li=[]
	for i in pro:
		if i.price<100:
			li.append(i)
	print(li)
	return render(request,'specialoffer.html',{'li':cart,'list':li})
def news(request):
	car=Cart.objects.all()
	cart=car.count()
	return render(request,'news.html',{'li':cart})
def babygift(request):
	car=Cart.objects.all()
	cart=car.count()
	baby=Product.objects.all()
	list=[]
	for i in baby:
		l={}
		print(i.category)
		if i.category=='babygift':
			l.update({'id':i.id,'name':i.product_name,'category':i.category,'price':i.price,'desc':i.desc,'image':i.Image})
			print(i.category)
			list.append(l)
		print(l)
	print(list)
	return render(request,'babygift.html',{'baby':list,'li':cart})
def birthdaygift(request):
	car=Cart.objects.all()
	cart=car.count()
	birthday=Product.objects.all()
	list=[]
	for i in birthday:
		l={}
		if i.category=="birthdaygift":
			l.update({'id':i.id,'name':i.product_name,'category':i.category,'price':i.price,'desc':i.desc,'image':i.Image})

			list.append(l)
		print(l)
	print(list)
	return render(request,'birthdaygift.html',{'birthday':list,'li':cart})
def cristamgift(request):
	car=Cart.objects.all()
	cart=car.count()
	baby=Product.objects.all()
	list=[]
	for i in baby:
		l={}
		if i.category=="cristamgift":
			l.update({'id':i.id,'name':i.product_name,'category':i.category,'price':i.price,'desc':i.desc,'image':i.Image})

			list.append(l)
		print(l)
	print(list)
	return render(request,'cristamgift.html',{'cristam':list,'li':cart})
def giftforher(request):
	car=Cart.objects.all()
	cart=car.count()
	baby=Product.objects.all()
	list=[]
	for i in baby:
		l={}
		if i.category=="giftforher":
			l.update({'id':i.id,'name':i.product_name,'category':i.category,'price':i.price,'desc':i.desc,'image':i.Image})

			list.append(l)
		print(l)
	print(list)
	return render(request,'giftforher.html',{'gf':list,'li':cart})
def giftforhim(request):
	car=Cart.objects.all()
	cart=car.count()
	baby=Product.objects.all()
	list=[]
	for i in baby:
		l={}
		if i.category=="giftforhim":
			l.update({'id':i.id,'name':i.product_name,'category':i.category,'price':i.price,'desc':i.desc,'image':i.Image})

			list.append(l)
		print(l)
	print(list)
	return render(request,'giftforhim.html',{'gm':list,'li':cart})
def toysgift(request):
	car=Cart.objects.all()
	cart=car.count()
	baby=Product.objects.all()
	list=[]
	for i in baby:
		l={}
		if i.category=="toysgift":
			l.update({'id':i.id,'name':i.product_name,'category':i.category,'price':i.price,'desc':i.desc,'image':i.Image})

			list.append(l)
		print(l)
	print(list)
	return render(request,'toysgift.html',{'toy':list,'li':cart})
def valentinegift(request):
	car=Cart.objects.all()
	cart=car.count()
	baby=Product.objects.all()
	list=[]
	for i in baby:
		l={}
		if i.category=="valentinegift":
			l.update({'id':i.id,'name':i.product_name,'category':i.category,'price':i.price,'desc':i.desc,'image':i.Image})

			list.append(l)
		print(l)
	print(list)
	return render(request,'valentinegift.html',{'valentine':list,'li':cart})
def accentsgift(request):
	car=Cart.objects.all()
	cart=car.count()
	baby=Product.objects.all()
	list=[]
	for i in baby:
		l={}
		if i.category=="accentsgift":
			l.update({'id':i.id,'name':i.product_name,'category':i.category,'price':i.price,'desc':i.desc,'image':i.Image})

			list.append(l)
		print(l)
	print(list)
	return render(request,'accentsgift.html',{'accents':list,'li':cart})
def artificialgift(request):
	car=Cart.objects.all()
	cart=car.count()
	baby=Product.objects.all()
	list=[]
	for i in baby:
		l={}
		if i.category=="artificialgift":
			l.update({'id':i.id,'name':i.product_name,'category':i.category,'price':i.price,'desc':i.desc,'image':i.Image})

			list.append(l)
		print(l)
	print(list)
	return render(request,'artificialgift.html',{'artgift':list,'li':cart})

def addproduct(request):

	if request.method=="POST":
		product=Product()
		product.product_name=request.POST['product_name']
		product.category=request.POST['category']
		product.subcategory=request.POST['subcategory']
		product.desc=request.POST['product_description']
		product.price=request.POST['price']
		product.pub_date=request.POST['pub_date']
		product.Image=request.FILES['image']
		product.save()
		return redirect('index')
	return render(request,'addproduct.html')

def editproduct(request,id):
	product=Product.objects.get(pk=id)
	if request.method=="POST":
		product.product_name=request.POST['product_name']
		product.category=request.POST['category']
		product.subcategory=request.POST['subcategory']
		product.desc=request.POST['product_description']
		product.price=request.POST['price']
		product.pub_date=request.POST['pub_date']
		product.Image=request.FILES['image']
		product.save()
		return redirect('index')
	return render(request,'editproduct.html',{'i':product})


def viewallproduct(request):
	allpro=Product.objects.all()
	return render(request,'viewallproduct.html',{'allpro':allpro})
def deleteproduct(request,id):
	product=Product.objects.get(pk=id)
	product.delete();
	return redirect('viewallproduct')


def viewproduct(request,id):
	car=Cart.objects.all()
	cart=car.count()
	product=Product.objects.get(pk=id)
	pro=Product.objects.all()
	li=[]
	for i in pro:
		if i.category == product.category:
			li.append(i)

	if request.user.is_authenticated:
		user=request.user.username
		print(user)
	return render(request,'viewproduct.html',{'products':product,'pro':li,'li':cart})


def cartitems(request):
	cart=Cart.objects.all()
	sum=0
	for i in cart:
		print(i.price)
		sum=sum+i.price
	print('Total: ',sum)
	return render(request,'cartitems.html',{'cart':cart,'total':sum})


def deletecartitem(request,id):
	cart=Cart.objects.get(pk=id)
	cart.delete();
	return redirect('cartitems')

def buynow(request,id):
	pr=Cart.objects.get(pk=id)
	if request.method=="POST":
		email=request.POST['email']
		name=request.POST['name']
		address1=request.POST['address1']
		address2=request.POST['address2']
		city=request.POST['city']
		state=request.POST['state']
		zip_code=request.POST['zip_code']
		product_details=pr.product_name
		order=Orders(email=email,name=name,address1=address1,address2=address2,city=city,state=state,zip_code=zip_code,product_details=product_details)
		order.save()
		pr.delete();
		return redirect('index')
	return render(request,'buynow.html')
