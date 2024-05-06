from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from UserApp.models import *


# Create your views here.

def home(request):
    total_products = ProductModel.objects.count()
    total_users = UserModel.objects.count()
    total_price = SpecificationModel.objects.aggregate(total_price=models.Sum('price'))['total_price'] or 0

    return render(request, 'admin_mainpage.html', {
        'total_products': total_products,
        'total_users': total_users,
        'total_price': total_price
    })


def add_products(request):
    brand = BrandModel.objects.all()
    category = CategoryModel.objects.all()
    condition = ProductConditionModel.objects.all()
    Image = ImageModel.objects.all()

    if request.method == "POST":
        new_product = ProductModel()
        new_product.product_id = request.POST.get('product_id')
        new_product.model_name = request.POST.get('model_name')
        new_product.model_number = request.POST.get('model_number')
        new_product.brand_id = BrandModel.objects.get(brand_id=request.POST.get('brand_id'))
        new_product.category_id = CategoryModel.objects.get(category_id=request.POST.get('category_id'))
        new_product.condition_id = ProductConditionModel.objects.get(condition_id=request.POST.get('condition_id'))
        new_product.image_id = ImageModel.objects.get(image_id=request.POST.get('image_id'))
        new_product.save()
        return redirect('add_specification')
    return render(request, 'adding_product_page1.html',
                  {'brand': brand, 'category': category, 'condition': condition, 'Image': Image})


def add_specification(request):
    products = ProductModel.objects.all()
    if request.method == "POST":
        new_product = SpecificationModel()
        new_product.product_id = ProductModel.objects.get(product_id=request.POST.get('product_id'))
        new_product.ram = request.POST.get('ram')
        new_product.rom = request.POST.get('rom')
        new_product.camera = request.POST.get('camera')
        new_product.battery = request.POST.get('battery')
        new_product.processor = request.POST.get('processor')
        new_product.price = request.POST.get('price')
        new_product.screen_size = request.POST.get('screen_size')
        new_product.model_name = request.POST.get('model_name')
        new_product.operating_system = request.POST.get('operating_system')
        new_product.version = request.POST.get('version')
        new_product.colour = request.POST.get('colour')
        new_product.save()
        return redirect('add_specification')
    return render(request, 'adding_specification.html', {'products': products})


def brand(request):
    category = CategoryModel.objects.all()
    if request.method == "POST":
        new_brand = BrandModel()
        new_brand.brand_name = request.POST.get('brand')
        new_brand.categor_id = CategoryModel.objects.get(category_id=request.POST.get('category'))
        new_brand.save()
        return redirect('add_product')
    return render(request, 'adding_brand.html', {'category': category})


def condition(request):
    if request.method == "POST":
        new_condition = ProductConditionModel()
        new_condition.condition_name = request.POST.get('condition_name')
        new_condition.save()
        return redirect('add_product')
    return render(request, 'adding_condition.html')


def category(request):
    if request.method == "POST":
        new_category = CategoryModel()
        new_category.category_name = request.POST.get('category_name')
        new_category.save()
        return redirect('add_product')
    return render(request, 'adding_category.html')


def images(request):
    categories = CategoryModel.objects.all()
    if request.method == "POST":
        new_image = ImageModel()
        new_image.images = request.FILES['images']
        new_image.img1 = request.FILES['img1']
        new_image.img2 = request.FILES['img2']
        new_image.img3 = request.FILES['img3']
        new_image.img_name = request.POST.get('image_name')
        new_image.category = CategoryModel.objects.get(category_id=request.POST.get('category'))
        new_image.save()
        return redirect('add_product')
    return render(request, 'adding_images.html', {'category': categories})


def products_list(request):
    products = ProductModel.objects.all()
    return render(request, 'products_lists.html', {'products': products})


def remove_products(request, product_id):
    try:
        product = get_object_or_404(ProductModel, product_id=product_id)
        product.delete()
        return redirect('products_list')
    except ProductModel.DoesNotExist:
        return HttpResponse("Product with the specified ID does not exist.", status=404)



def add_user(request):
    users = UserModel.objects.all()
    if request.method == 'POST':
        new_user = UserModel()
        new_user.user_name = request.POST.get('username')
        new_user.phone_number = request.POST.get('phone')
        new_user.email = request.POST.get('email')
        new_user.password = request.POST.get('password')
        new_user.save()
        return redirect('add_users')
    return render(request, 'add_users.html', {'users': users})


def users_list(request):
    users = UserModel.objects.all()
    return render(request, 'remove_users.html', {'users': users})


def remove_users(request, user_id):
    user = UserModel.objects.get(user_id=user_id)
    user.delete()
    return redirect('users_list')
