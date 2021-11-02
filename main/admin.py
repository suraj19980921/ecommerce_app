from django.contrib import admin
from main import models

# Register your models here.

admin.site.register([
    models.Shop,
    models.Item,
    models.Category,
    models.Order,
    models.Cart
])
