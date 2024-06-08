# Generated by Django 5.0.6 on 2024-06-05 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0011_rename_unit_price_salesorderdetail_selling_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='shipping_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Shipping fee for the order', max_digits=10),
        ),
        migrations.AlterField(
            model_name='sale',
            name='payment_status',
            field=models.CharField(blank=True, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], max_length=50, null=True),
        ),
    ]
