from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from listbook.models import Book
from .models import CartItem, Cart

# Create your views here.
def cardID(request):
    card_id = request.session.session_key
    if not card_id:
        card_id = request.session.create()
    return card_id

def add_cart(request, book_id, qtt):
    user = request.user
    book = Book.objects.get(id=book_id)
    quantity = qtt
    if user.is_authenticated:
        is_exists_cart_item = CartItem.objects.filter(book=book, user=user).exists() and (quantity <= book.inStock)
        if is_exists_cart_item:
            cart_item = CartItem.objects.filter(
                book=book,
                user=user,
            )
            cart_item.quantity += quantity
        else:
            cart_item = CartItem.objects.create(
                book=book,
                user=user,
                quantity=quantity
            )
        cart_item.save()
        return redirect('cart')
    
    else:
        return redirect('login')

def change_quantity(request, book_id, cart_item_id, qtt):
    book = Book.objects.get(id=book_id)
    quantity = qtt

    is_exists_cart_item = CartItem.objects.filter(id=cart_item_id, book=book).exists() and (quantity <= book.inStock)
    if is_exists_cart_item:
        cart_item = CartItem.objects.filter(
            book=book,
            id=cart_item_id
        )
        cart_item.quantity = quantity
    elif quantity > book.inStock:
        return change_quantity(request, book_id, cart_item_id, book.inStock)
    else:
        return ObjectDoesNotExist
    cart_item.save()
    return redirect('cart')

def cart(request, total=0, quantity=0, cart_items=None):
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=cardID(request=request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += cart_item.total()
            quantity += cart_item.quantity
    except ObjectDoesNotExist:
        pass    # Chỉ bỏ qua
    print(request.user)
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
    }
    return render(request, 'cart.html', context=context)


