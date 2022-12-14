from django.shortcuts import render, redirect
from listbook.models import Book
from django.contrib.auth.decorators import login_required
from user_cart.models import Cart, CartItem

@login_required(login_url="/login")
def cart_add(request, id):
    current_user = request.user
    try:
        cart = Cart.objects.get(user_id=current_user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            user_id = current_user
        )
    cart.save()

    book = Book.objects.get(id=id)
    new_book = CartItem.objects.create(
        book=book,
        cart=cart,
        is_active=True
    )
    return redirect("/cart/cart-detail")


@login_required(login_url="/login")
def item_clear(request, id):
    current_user = request.user
    cart = Cart.objects.get(user_id=current_user)
    book = Book.objects.get(id=id)
    product = CartItem.objects.get(cart=cart, book=book)
    product.delete()
    return redirect("/cart/cart-detail")

@login_required(login_url="/login")
def cart_detail(request):
    is_cart_exist = Cart.objects.filter(user_id=request.user).exists()
    if is_cart_exist:
        cart = Cart.objects.get(user_id=request.user)
        list_item = CartItem.objects.filter(cart=cart)
        number = list_item.count()
        if number == 0:
            cart.delete()
            return render(request, 'cart.html', {
                'exist': is_cart_exist
                })
        return render(request, 'cart.html', {
            'exist': is_cart_exist, 
            'list_item': list_item
        })
    return render(request, 'cart.html', {
        'exist': is_cart_exist
        })
