# Generated by Django 3.2.8 on 2021-11-08 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('All', '0005_auto_20211108_0409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='books',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderbook',
            name='Book',
        ),
        migrations.RemoveField(
            model_name='orderbook',
            name='user',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='orderbook',
        ),
    ]