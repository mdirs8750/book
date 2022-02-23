from unicodedata import name
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('admin', admin.site.urls),
    path("",views.home, name="home"),
    #path("home",views.home,name="home"),    
    path("about/",views.about, name="about"),

    
    
    path("test/",views.test, name="test"),
    
    
    
    path("signup",views.signup,name="signup"),
    path("login",views.login, name="login"),
    #path("log_v",views.log_v,name="log_v")

    path('logout',views.logout, name="logout"),

    path('cart',views.cart,name="cart"),

    #for checkout for payment
    path('checkout',views.checkout,name="checkout"),

    #for order details page
    path('order',views.orderd,name="order")
]
