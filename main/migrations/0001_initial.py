# Generated by Django 5.0.2 on 2024-03-14 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.TimeField(auto_created=True, verbose_name='yaratish')),
                ('full_name', models.CharField(max_length=150, verbose_name='Mahsulotnign nomi')),
                ('brand', models.CharField(max_length=255, verbose_name='brandi')),
                ('seller', models.CharField(max_length=255, verbose_name='sotuvchi')),
                ('subcategory', models.CharField(max_length=255, verbose_name='kataqgoryiasi')),
                ('tag', models.CharField(max_length=255, verbose_name='qoshimcha')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='narh')),
                ('delivery_date', models.DateTimeField(blank=True, null=True, verbose_name='buyurtma kuni')),
                ('order_code', models.CharField(max_length=255, verbose_name='zakaz codi')),
                ('images', models.ImageField(upload_to='product_photo/', verbose_name='rasim')),
                ('quantity', models.IntegerField(default=0, verbose_name='miqdori')),
                ('is_sale', models.BooleanField(default=False, verbose_name='sotilmoqda')),
                ('old_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='eski narhi')),
                ('sale_expire', models.DateTimeField(blank=True, null=True, verbose_name='sotish muddati tugashi')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Mahsulot',
            },
        ),
    ]