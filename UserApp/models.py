
from django.db import models
from AdminApp.models import *


# Create your models here.
# User registration

class UserModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'user_details'




# User cart

class CartModel(models.Model):
    cart_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    spec_id = models.ForeignKey(SpecificationModel, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_created=True)

    class Meta:
        db_table = 'cart_table'




# User Favourite
class FavouriteModel(models.Model):
    favorite_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    spec_id = models.ForeignKey(SpecificationModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'favourite_table'


# User Address
class UserAddressModel(models.Model):
    address_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=50,null=True)
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    alternative_phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=300,null=True)
    landmark = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)

    class Meta:
        db_table = 'user_address_table'


# User order

class OrderModel(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    spec_id = models.ForeignKey(SpecificationModel, on_delete=models.CASCADE)
    address_id = models.ForeignKey(UserAddressModel, on_delete=models.CASCADE, null=True)
    quantity = models.CharField(max_length=100,blank=True,null=True)
    order_date = models.DateTimeField(auto_created=True)

    class Meta:
        db_table = 'oder_table'


# User Feedback

class FeedbackModel(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    spec_id = models.ForeignKey(SpecificationModel, on_delete=models.CASCADE, null=True)
    feedback_date = models.DateTimeField(auto_created=True)
    feedback_text = models.CharField(max_length=600)

    class Meta:
        db_table = 'feedback_table'


