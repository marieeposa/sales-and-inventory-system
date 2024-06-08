# Generated by Django 5.0.6 on 2024-06-05 15:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0010_salesorderdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salesorderdetail',
            old_name='unit_price',
            new_name='selling_price',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='payment_terms',
        ),
        migrations.AlterField(
            model_name='sale',
            name='order_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]