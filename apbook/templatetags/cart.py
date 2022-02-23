
from ast import Return
from atexit import register
from django import template


register=template.Library()

@register.filter(name='isexistincart')
def isexistincart(product,cart):
    keys= cart.keys()
    for id in keys:
        if int(id)== product.id:
            return True
    return False



#for showing the quantity of product in the card
@register.filter(name="cartquant")
def cartquant(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id)== product.id:
            return cart.get(id)
    return False

@register.filter(name="totalprice")
def totalprice(product,cart):
    return product.price * cartquant(product,cart)

@register.filter(name="grand_total")
def grand_total(product,cart):
    s=0
    for p in product:
        s+=totalprice(p,cart)
    return s

@register.filter(name="total")
def total(price,quantity):
    return price*quantity

# @register.filter(name="payamount")
# def payamount(totalprice,cart,c = {'a':0}):
    
#     c['a'] = totalprice*cart
#     print(c)
