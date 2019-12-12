# Generated by Django 2.0.6 on 2019-12-05 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20190924_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverhardware',
            name='purchase_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Alış qiməti'),
        ),
        migrations.AlterField(
            model_name='serverhardware',
            name='selling_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Satış qiyməti'),
        ),
    ]