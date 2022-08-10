from ast import Return
import email
from os import remove
from unicodedata import category
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from sympy import Order
from .models import clnt_info, order, product, Category
from django.contrib.auth.models import User

#for password validations
from django.contrib.auth.hashers import make_password,check_password
#end

#for api root strt
from rest_framework import routers, serializers, viewsets
#end

#for sending email as greeting
from django.core.mail import send_mail

from .serializer import demo_restframe, restframework

# Create your views here.
def base(request):
    return render(request,'base.html')

def home(request):

    

    nam = None
    request.session['checkcart']=0
    # nam=request.session['email']
    
    #    # request.session.modifiesd = true
    # context={
    #     'name':nam
    # }
    
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

#for signup form
def signup(request):
    if request.method == "POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        eml=request.POST.get('email')
        phn=request.POST.get('phone')
        pwd=request.POST.get('password')
        gen=request.POST.get('gender')
        #print(fname,lname,eml,phn)
        d=clnt_info(firstname=fname,lastname=lname,phone=phn,emails=eml,password=make_password(pwd),gender=gen)
        d.save()
        #for sending email as greeting strt
        # send_mail(
        #     "thanks for signing up ",
        #     'welcome to ebook shop created by MD irshad',
        #     "faizan7860md@gmail.com",
        #     [eml] 
        # )
        
        #greeting eamil end
        return redirect('home')
    return render (request,'home.html')




#for fetching the details of client and admin
def login(request):
    error_msg = None
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        try:
            fetch_email = clnt_info.objects.get(emails=email)
            if (fetch_email.emails == email):        
                flag = check_password(password, fetch_email.password)
                if flag:
                    request.session['email'] = email
                    request.session['firstname'] = fetch_email.firstname
                    request.session['customer_id'] = fetch_email.id
                    return redirect('home')
                else:
                    error_msg = "Please Enter valid password"
                    return render(request, 'home.html', {'error_msg': error_msg})
        except:
            error_msg = "invalid email"
            return render(request, 'home.html', {'error_msg': error_msg})



def test(request):
    path=None
    # request.session['checkcart']=0

    if request.method =="POST":
        request.session['checkcart']=1
        product_id=request.POST.get('cartid')
        remove = request.POST.get('minus')

        cart_id=request.session.get('cart')

        if cart_id:
            quantity= cart_id.get(product_id)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart_id.pop(product_id)
                    else:
                        cart_id[product_id] = quantity -1                
                else:
                    cart_id[product_id] =quantity +1
            else:
                cart_id[product_id] = 1
        else:
            cart_id= {}
            cart_id[product_id] = 1

        request.session['cart']=cart_id
        print(request.session['cart'])
    
    img=product.objects.all()
    cat=Category.objects.all()

    cat_id =request.GET.get(category)
    if cat_id:
        path =product.objects.filter(category_id=cat_id)
    else:
        path= product.objects.all()

    return render(request,'testing.html', {'imge':path,'cate':cat})

def logout(request):
    request.session.clear()
    return redirect ('home') 

def cart(request):
    try:
        # if request.session['checkcart']==1:

        p=list(request.session.get('cart').keys())
        f=product.objects.filter(id__in=p)
            
        return render(request,'cart.html',{"f":f})
    except:
        return render(request,'cart.html')
    

def checkout(request):
    if request.method =="POST":
        address=request.POST.get("address")
        phoneno=request.POST.get("phoneno")
        customer_id=request.session.get("customer_id")
        cart= request.session.get("cart")
        products=product.objects.filter(id__in=list(cart.keys()))

        for pro in products:
            save_order_dtls=order(
                customer=clnt_info(id=customer_id),
                product=pro,
                price=pro.price,
                quantity=cart.get(str(pro.id)),
                Address=address,
                phoneno=phoneno)
            print(address,products,cart,customer_id,phoneno)
            save_order_dtls.save()
            request.session['cart']={}
             
            
    return redirect('cart')



# for order details
def orderd(request):
    customer=request.session['customer_id']
    orderdtl=order.objects.filter(customer=customer).order_by('-date')
    print(orderdtl)
    # request.session['order']=orderdtl
    c = 0
    for i in orderdtl:
        c += i.price*i.quantity
    print(c)

    

    return render(request,'orddtl.html',{'orderdtl':orderdtl,'c':c})


def chk(request):
    return render(request,'check.html')


#for api root                   
class demorestframe(viewsets.ModelViewSet):
    queryset = restframework.objects.all()
    serializer_class = demo_restframe
