# Generated by Django 2.0.6 on 2019-09-24 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkhardware',
            name='description',
            field=models.TextField(default=None, max_length=500, verbose_name='Təsvir'),
        ),
    ]
