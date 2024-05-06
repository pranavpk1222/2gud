from django.db import models


# Admin log in
# Create your models here.
class AdminModel(models.Model):
    admin_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)

    class Meta:
        db_table = 'admin_detail'


class CategoryModel(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'category_table'


class BrandModel(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=100)
    categor_id = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.brand_name

    class Meta:
        db_table = 'brand_table'


class ProductConditionModel(models.Model):
    condition_id = models.AutoField(primary_key=True)
    condition_name = models.CharField(max_length=50)

    def __str__(self):
        return self.condition_name

    class Meta:
        db_table = 'condition_table'


# Images

class ImageModel(models.Model):
    image_id = models.AutoField(primary_key=True)
    images = models.ImageField(upload_to='images')
    img1 = models.ImageField(upload_to='images', null=True, blank=True)
    img2 = models.ImageField(upload_to='images', null=True, blank=True)
    img3 = models.ImageField(upload_to='images', null=True, blank=True)
    img_name = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_images'


# Product
class ProductModel(models.Model):
    product_id = models.CharField(max_length=20, primary_key=True)
    model_name = models.CharField(max_length=35)
    model_number = models.CharField(max_length=35)
    brand_id = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    category_id = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    condition_id = models.ForeignKey(ProductConditionModel, on_delete=models.CASCADE)
    image_id = models.ForeignKey(ImageModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.model_name

    class Meta:
        db_table = 'product_table'


# Specification
class SpecificationModel(models.Model):
    spec_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    ram = models.CharField(max_length=20)
    rom = models.CharField(max_length=20)
    camera = models.CharField(max_length=100, null=True)
    battery = models.CharField(max_length=100, null=True)
    processor = models.CharField(max_length=150)
    price = models.IntegerField()
    screen_size = models.CharField(max_length=250, null=True)
    model_name = models.CharField(max_length=100, null=True)
    operating_system = models.CharField(max_length=100, null=True)
    version = models.CharField(max_length=100, null=True)
    colour = models.CharField(max_length=50)

    def __str__(self):
        return self.model_name

    class Meta:
        db_table = 'specification_table'


# Event
class EventModel(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=100)
    event_img = models.ImageField(upload_to='images', null=True)
    event_start_date = models.DateField()
    event_end_date = models.DateField()

    def __str__(self):
        return self.event_name

    class Meta:
        db_table = 'event_table'


# Discount

class DiscountModel(models.Model):
    event_id = models.ForeignKey(EventModel, on_delete=models.CASCADE)
    product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    up_to = models.CharField(max_length=20)

    def __str__(self):
        return self.product_id.model_name

    class Meta:
        db_table = 'discount_table'
