# Generated by Django 5.0.4 on 2024-05-13 05:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('transactions', '0002_alter_purchase_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='supplier',
            field=models.ForeignKey(db_column='supplier_id', on_delete=django.db.models.deletion.CASCADE, to='accounts.supplier'),
        ),
    ]
