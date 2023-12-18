from rest_framework import serializers
from .models import Produk, Kategori, Status

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class ProdukSerializer(serializers.ModelSerializer):
    kategori = KategoriSerializer()
    status = StatusSerializer()

    class Meta:
        model = Produk
        fields = '__all__'

    def create(self, validated_data):
        # Create a new Produk instance and related Kategori and Status instances
        kategori_data = validated_data.pop('kategori', {})
        status_data = validated_data.pop('status', {})

        kategori_instance = Kategori.objects.create(**kategori_data)
        status_instance = Status.objects.create(**status_data)

        produk_instance = Produk.objects.create(kategori=kategori_instance, status=status_instance, **validated_data)
        return produk_instance
        
    def update(self, instance, validated_data):
        # Update the fields of the Produk instance
        instance.nama_produk = validated_data.get('nama_produk', instance.nama_produk)
        instance.harga = validated_data.get('harga', instance.harga)

        # Update the related Kategori instance
        kategori_data = validated_data.get('kategori', {})
        kategori_instance = instance.kategori
        kategori_instance.nama_kategori = kategori_data.get('nama_kategori', kategori_instance.nama_kategori)
        kategori_instance.save()

        # Update the related Status instance
        status_data = validated_data.get('status', {})
        status_instance = instance.status
        status_instance.nama_status = status_data.get('nama_status', status_instance.nama_status)
        status_instance.save()

        instance.save()
        return instance
