from datetime import datetime, date

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from UserApp.models import *
from AdminApp.models import *
from django.db.models import Q


def home(request):
    smartphone = ProductModel.objects.filter(category_id=4)
    laptop = ProductModel.objects.filter(category_id=5)
    tab = ProductModel.objects.filter(category_id=6)
    dropdown_smartphone = BrandModel.objects.filter(categor_id=4)
    dropdown_laptop = BrandModel.objects.filter(categor_id=5)
    dropdown_tab = BrandModel.objects.filter(categor_id=6)


    return render(request, 'homepage.html', {'product': smartphone, 'tab': tab, 'laptop': laptop,
                                             'dropdown_smartphone': dropdown_smartphone,
                                             'dropdown_laptop': dropdown_laptop,
                                             'dropdown_tab': dropdown_tab})


def search(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        sort_value = request.POST.get('sort')

        if query:
            # Perform search across ProductModel and SpecificationModel
            products = ProductModel.objects.filter(model_name__icontains=query)
            specifications = SpecificationModel.objects.filter(product_id__model_name__icontains=query)

            # Sorting specifications based on price
            if sort_value == 'asc':
                specifications = specifications.order_by('price')
            elif sort_value == 'desc':
                specifications = specifications.order_by('-price')
            else:
                # If sort_value is not provided or invalid, default to ascending order
                specifications = specifications.order_by('price')

            return render(request, 'searchpage.html',
                          {'products': products, 'specifications': specifications})
        else:
            # Handle case when query is empty
            return render(request, 'searchpage.html', {'error_message': 'Please enter a search query'})
    else:
        # Handle case when request method is not POST
        return HttpResponse("Method not allowed", status=405)







def product_details(request, product_id):
    spec_data = SpecificationModel.objects.filter(product_id=product_id)
    product = ProductModel.objects.filter(product_id=product_id)
    reviews = FeedbackModel.objects.filter(spec_id=spec_data[0].spec_id)

    return render(request, 'product_view.html', {'spec_data': spec_data,

                                                 'product': product, 'reviews': reviews})



def user_register(request):
    if request.method == 'POST':
        new_user = UserModel()
        new_user.user_name = request.POST.get('username')
        new_user.phone_number = request.POST.get('phone')
        new_user.email = request.POST.get('email')
        new_user.password = request.POST.get('password')
        new_user.save()
        return redirect('login')
    return render(request, 'user_registration.html')







def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = UserModel.objects.filter(user_name=username, password=password).first()
        if user:
            request.session['user_id'] = user.user_id
            return redirect('/')
        else:
            redirect('/login')

    return render(request, 'log_in.html')


def cart(request, spec_id):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        if request.method == 'POST':
            quantity = request.POST.get('quantity')
            spec = SpecificationModel.objects.get(spec_id=spec_id)

            # Check if the cart item already exists for the user and product
            cart_item = CartModel.objects.filter(user_id=user_id, spec_id=spec).first()
            if cart_item:
                # If the cart item exists, update its quantity
                cart_item.quantity += int(quantity)
                cart_item.save()
            else:
                # If the cart item does not exist, create a new one
                cart_item = CartModel.objects.create(
                    user_id_id=user_id,
                    spec_id=spec,
                    quantity=quantity,
                    create_at=datetime.now()
                )
                cart_item.save()

            return render(request, 'animation.html')
        else:
            return redirect('detail', spec_id=spec_id)
    else:
        return redirect('/login')


def cart_show(request):
    if 'user_id' in request.session:
        cart = CartModel.objects.filter(user_id=request.session['user_id']).all()
        return render(request, 'cart_show.html', {'cart': cart})
    else:
        return redirect('/login')


def logout(request):
    if 'user_id' in request.session:
        user = request.session['user_id']
        print(user)
        del request.session['user_id']
    return redirect('/login')


def remove_cart(request, cart_id):
    data = CartModel.objects.get(cart_id=cart_id)
    data.delete()
    return redirect('/cart_store')


def wishlist(request, product_id):
    if 'user_id' in request.session:
        if request.method == 'GET':
            user_id = request.session['user_id']
            spec = SpecificationModel.objects.get(product_id=product_id)
            wish = FavouriteModel()
            wish.user_id_id = user_id
            wish.spec_id = spec
            wish.save()
            return redirect('detail', product_id=product_id)
        else:
            return HttpResponse('unable to add wishlist')
    return redirect('/login')


def wishlist_store(request):
    if 'user_id' in request.session:
        my_data = UserModel.objects.filter(user_id=request.session['user_id'])
        wish = FavouriteModel.objects.filter(user_id=request.session['user_id']).all()
        return render(request, 'wishlist.html', {'wishlist': wish, 'my_data': my_data})


def remove_wishlist(request, favorite_id):
    data = FavouriteModel.objects.get(favorite_id=favorite_id)
    data.delete()
    return redirect('/wish_store')


def profile(request):
    if 'user_id' in request.session:
        my_data = UserModel.objects.filter(user_id=request.session['user_id'])
        if request.method == 'POST':
            update = UserModel()
            update.user_id = request.session['user_id']
            update.user_name = request.POST.get('user_name')
            update.phone_number = request.POST.get('ph_no')
            update.email = request.POST.get('email')
            update.password = request.POST.get('password')
            update.create_at = datetime.now()
            update.save()
            return redirect('/')
        return render(request, 'profile.html', {'my_data': my_data})


def address(request):
    if 'user_id' in request.session:
        my_data = UserModel.objects.filter(user_id=request.session['user_id'])
        my_address = UserAddressModel.objects.filter(user_id=request.session['user_id'])
        return render(request, 'address.html', {'my_data': my_data, 'my_address': my_address})


def update_address(request, address_id):
    if 'user_id' in request.session:
        my_data = UserModel.objects.filter(user_id=request.session['user_id'])
        my_address = UserAddressModel.objects.filter(address_id=address_id)
        if request.method == 'POST':
            change = UserAddressModel.objects.get(user_id=request.session['user_id'], address_id=address_id)
            change.user_id_id = request.session['user_id']
            change.address_type = request.POST.get('address_type')
            change.full_name = request.POST.get('full_name')
            change.phone_number = request.POST.get('ph_no')
            change.alternative_phone_number = request.POST.get('ph_no2')
            change.address = request.POST.get('address')
            change.landmark = request.POST.get('landmark')
            change.pin_code = request.POST.get('pin_code')
            change.save()
            return redirect('/address')

        return render(request, 'update_address.html', {'my_data': my_data, 'my_address': my_address})


def new_address(request):
    if 'user_id' in request.session:
        my_data = UserModel.objects.filter(user_id=request.session['user_id'])
        if request.method == 'POST':
            address = UserAddressModel()
            address.user_id_id = request.session['user_id']
            address.address_type = request.POST.get('Address_type')
            address.full_name = request.POST.get('full_name')
            address.phone_number = request.POST.get('ph_no1')
            address.alternative_phone_number = request.POST.get('ph_no2')
            address.address = request.POST.get('address')
            address.landmark = request.POST.get('Landmark')
            address.pin_code = request.POST.get('pin_code')
            address.save()
            return redirect('/address')
        return render(request, 'newaddress.html', {'my_data': my_data})


def remove_address(request, address_id):
    data = UserAddressModel.objects.get(address_id=address_id)
    data.delete()
    return redirect('/address')


def order_first(request, spec_id):
    if 'user_id' in request.session:
        spec = SpecificationModel.objects.filter(spec_id=spec_id)
        user = UserModel.objects.filter(user_id=request.session['user_id'])
        address = UserAddressModel.objects.filter(user_id=request.session['user_id'])
        return render(request, 'order_first_page.html', {'specs': spec, 'user': user, 'address': address})
    else:
        return redirect('/')


def ordering_products(request, spec_id):
    if request.method == 'POST':
        print(request.method)
        spec = SpecificationModel.objects.get(
            spec_id=spec_id)  # Use get() instead of filter() if you expect only one result
        my_order = OrderModel()
        my_order.user_id = UserModel.objects.get(user_id=request.session['user_id'])
        my_order.spec_id = spec
        my_order.address_id = UserAddressModel.objects.get(address_id=request.POST.get('address'))
        my_order.quantity = request.POST.get('quantity')
        my_order.order_date = datetime.now()
        my_order.save()
        return render(request, 'order_success_animation.html')
    else:
        return HttpResponse('Method not allowed')


def my_orders(request):
    my_data = UserModel.objects.filter(user_id=request.session['user_id'])
    my_order = OrderModel.objects.filter(user_id=request.session['user_id']).all()
    return render(request, 'my_order.html', {'my_orders': my_order, 'my_data': my_data})


def review_order(request, spec_id):
    if 'user_id' in request.session:
        user = UserModel.objects.filter(user_id=request.session['user_id'])
        spec = SpecificationModel.objects.filter(spec_id=spec_id)

        existing_order = OrderModel.objects.filter(spec_id=spec_id, user_id=user.first())
        if existing_order.exists():
            if request.method == 'POST':
                myfeedback = FeedbackModel()
                myfeedback.user_id_id = request.session['user_id']
                myfeedback.spec_id = SpecificationModel.objects.get(spec_id=spec_id)
                myfeedback.feedback_date = datetime.now()
                myfeedback.feedback_text = request.POST.get('feedback')
                myfeedback.save()
                return redirect('/')

        else:
            return render(request, 'purchase_first.html')

        return render(request, 'review.html', {'spec_id': spec, 'order': user})
    else:
        return redirect('/login')


def event(request):
    # Filter events where the end date is greater than or equal to today's date
    current_events = EventModel.objects.filter(event_end_date__gte=date.today())
    return render(request, 'eventpage.html', {'events': current_events})


def super_sale(request, event_id):
    offer = DiscountModel.objects.filter(event_id=event_id)
    img = EventModel.objects.filter(event_id=event_id)
    return render(request, 'disccountpage1.html', {'offer': offer,'img':img})


def summer_sales(request, event_id):
    data = DiscountModel.objects.filter(event_id=event_id)
    img = EventModel.objects.filter(event_id=event_id)
    return render(request, 'summersale_page.html', {'offer': data,'img':img})
