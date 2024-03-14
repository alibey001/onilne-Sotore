import qrcode
from io import BytesIO
from django.db import models
from django.core.files import File
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser




class Product(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='Mahsulotnign nomi')
    brand = models.CharField(max_length=255, verbose_name='brandi')
    seller = models.CharField(max_length=255, verbose_name='sotuvchi')
    subcategory = models.CharField(max_length=255, verbose_name='kataqgoryiasi')
    tag = models.CharField(max_length=255,verbose_name='qoshimcha')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='narh')
    delivery_date = models.DateTimeField(null=True, blank=True, verbose_name='buyurtma kuni')
    order_code = models.CharField(max_length=255,verbose_name='zakaz codi')
    images = models.ImageField(upload_to='product_photo/', verbose_name='rasim')
    quantity = models.IntegerField(default=0, verbose_name='miqdori')
    is_sale = models.BooleanField(default=False, verbose_name='sotilmoqda')
    old_cost = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2, verbose_name='eski narhi')
    sale_expire = models.DateTimeField(null=True, blank=True, verbose_name='sotish muddati tugashi')
    created_at = models.TimeField(auto_created=True, verbose_name='yaratish')


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Mahsulot'


    def __str__(self):
        return self.full_name
