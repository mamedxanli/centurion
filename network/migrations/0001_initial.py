# Generated by Django 2.0.6 on 2019-09-23 21:00

from django.db import migrations, models
import network.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkHardware',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(default=None, max_length=100)),
                ('code', models.IntegerField(primary_key=True, serialize=False, verbose_name='Kod')),
                ('brand', models.CharField(default=None, max_length=20, verbose_name='Brend')),
                ('model', models.CharField(max_length=50, verbose_name='Model')),
                ('category', models.CharField(default=None, max_length=30, verbose_name='Kateqoriya')),
                ('description', models.CharField(default=None, max_length=100, verbose_name='Təsviri')),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Alış qiməti')),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Satış qiyməti')),
                ('quantity', models.IntegerField(default=1, verbose_name='Ədəd')),
                ('image', models.FileField(blank=True, default=None, upload_to=network.models.save_directory_path, verbose_name='Şəkil')),
                ('sold', models.BooleanField(default=False, verbose_name='Satılıb')),
                ('inventory', models.BooleanField(default=False, verbose_name='Inventar')),
            ],
            options={
                'verbose_name_plural': 'Şəbəkə avadanlıqları',
            },
        ),
    ]
