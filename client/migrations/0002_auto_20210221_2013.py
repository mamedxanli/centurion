# Generated by Django 2.2.13 on 2021-02-21 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='description',
            field=models.TextField(default=None, max_length=500, verbose_name='Təsvir'),
        ),
        migrations.AlterField(
            model_name='client',
            name='debt',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Borc'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(default=None, max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Müştərinin adı'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(default=None, max_length=30, verbose_name='Telefon'),
        ),
    ]
