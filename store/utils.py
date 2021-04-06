import json
from .models import *


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
        print('Cart:', cart)
    items = []
    order = {'get_card_total': 0, 'get_card_item': 0}
    CartItems = order['get_card_item']

    for i in cart:
        try:
            CartItems += cart[i]['quantity']

            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            order['get_card_total'] += total
            order['get_card_item'] += cart[i]['quantity']

            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL
                },
                'quantity': cart[i]['quantity'],
                'get_total': total
            }
            items.append(item)
            if product.digital == False:
                order['shipping'] = True
        except:
            pass
    return {'cartItems': CartItems, 'order': order, 'items': items}


def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        CartItems = order.get_card_item
    else:
        cookieData = cookieCart(request)
        CartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {'cartItems': CartItems, 'order': order, 'items': items}


def guestOrder(request, data):
    return ''
