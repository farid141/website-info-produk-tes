from django.contrib import admin
from .models import Produk, Kategori, Status

# Register your models here.
admin.site.register([Produk, Kategori, Status])