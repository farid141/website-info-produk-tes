from django.urls import path
from . import views

#buat variabel
urlpatterns=[
	path('produk/', views.produk, name='produk'),
    path('delete_produk/<int:pk>', views.delete_produk, name='delete_produk'),
    path('insert_produk/', views.insert_produk, name='insert_produk'),
    path('update_produk/<int:pk>', views.update_produk, name='update_produk'),
	path('produk_bisa_dijual/', views.produk_bisa_dijual, name='produk_bisa_dijual'),
]