# Generated by Django 2.0.6 on 2019-09-23 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(default=None, max_length=100)),
                ('name', models.CharField(max_length=30, verbose_name='Имя клиента')),
                ('phone', models.CharField(default=None, max_length=30, verbose_name='Телефон')),
                ('email', models.EmailField(default=None, max_length=254, verbose_name='Электронный адрес')),
                ('debt', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Долг')),
            ],
            options={
                'verbose_name_plural': 'Clients',
            },
        ),
    ]
