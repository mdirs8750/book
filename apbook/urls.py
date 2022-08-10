from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from .import views


#for api url
from apbook.views import demorestframe
from rest_framework import routers, serializers, viewsets

router=routers.DefaultRouter()
router.register(r'users',demorestframe,basename='MyModel')

urlpatterns = [
    path('admin', admin.site.urls),
    path("",views.home, name="home"),
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
    path('order',views.orderd,name="order"),

    path('chk',views.chk,name="chk"),

    #for api url
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
