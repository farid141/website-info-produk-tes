# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Kategori(models.Model):
    id_kategori = models.AutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'kategori'

    def __str__(self):
        return self.nama_kategori

class Status(models.Model):
    id_status = models.AutoField(primary_key=True)
    nama_status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'status'
    def __str__(self):
        return self.nama_status


class Produk(models.Model):
    id_produk = models.AutoField(primary_key=True)
    nama_produk = models.CharField(max_length=120, blank=True, null=True)
    harga = models.PositiveIntegerField(blank=True, null=True)
    kategori = models.ForeignKey(Kategori, models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey(Status, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'produk'