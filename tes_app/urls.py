from django.urls import path
from . import views
from . import api_views

#buat variabel
urlpatterns=[
	path('produk/', views.produk, name='produk'),
    path('delete_produk/<int:pk>', views.delete_produk, name='delete_produk'),
    path('insert_produk/', views.insert_produk, name='insert_produk'),
    path('update_produk/<int:pk>', views.update_produk, name='update_produk'),
	path('produk_bisa_dijual/', views.produk_bisa_dijual, name='produk_bisa_dijual'),
	path('api/produk/', api_views.produk_api, name='produk_api'),
	path('api/insert_produk/', api_views.insert_produk_api, name='insert_produk_api'),
    path('api/update_produk/<int:pk>/', api_views.update_produk_api, name='update_produk_api'),
    path('api/delete_produk/<int:pk>/', api_views.delete_produk_api, name='delete_produk_api'),
]