from django.contrib import admin
from UserApp.models import *

admin.site.register(UserModel)
admin.site.register(CartModel)
admin.site.register(FavouriteModel)
admin.site.register(UserAddressModel)
admin.site.register(OrderModel)
admin.site.register(FeedbackModel)

# Register your models here.
