from django.urls import path
from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.register,name='register'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('change_password/', views.change_password,name='change_password'),
    path('myaccount/', views.myaccount,name='myaccount'),
    path('checkout/', views.checkout,name='checkout'),
    path('delivery/', views.delivery,name='delivery'),
    path('vieworder/', views.vieworder,name='vieworder'),
    path('', views.index,name='index'),
    path('contact/', views.contact,name='contact'),
    path('news/', views.news,name='news'),
    path('newproducts/', views.newproducts,name='newproducts'),
    path('location/', views.location,name='location'),
    path('shoppingcart/', views.shoppingcart,name='shoppingcart'),
    path('specialoffer/', views.specialoffer,name='specialoffer'),
    path('faq/', views.faq,name='faq'),
    path('babygift/', views.babygift,name='babygift'),
    path('birthdaygift/', views.birthdaygift,name='birthdaygift'),
    path('cristamgift/', views.cristamgift,name='cristamgift'),
    path('accentsgift/', views.accentsgift,name='accentsgift'),
    path('toysgift/', views.toysgift,name='toysgift'),
    path('artificialgift/', views.artificialgift,name='artificialgift'),
    path('valentinegift/', views.valentinegift,name='valentinegift'),
    path('giftforher/', views.giftforher,name='giftforher'),
    path('giftforhim/', views.giftforhim,name='giftforhim'),
    path('addproduct/', views.addproduct,name='addproduct'),
    path('editproduct/<id>', views.editproduct,name='editproduct'),
    path('viewallproduct/', views.viewallproduct,name='viewallproduct'),
    path('deleteproduct/<id>', views.deleteproduct,name='deleteproduct'),
    path('viewproduct/<id>', views.viewproduct,name='viewproduct'),
    path('cart/<id>', views.cart,name='cart'),
    path('deletecartitem/<id>', views.deletecartitem,name='deletecartitem'),
    path('cartitems/', views.cartitems,name='cartitems'),
    path('buynow/<id>', views.buynow,name='buynow'),
]