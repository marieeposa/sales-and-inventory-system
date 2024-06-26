# Generated by Django 5.0.4 on 2024-06-07 08:36

import django.db.models.deletion
import django.utils.timezone
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_remove_invoice_customer_name_and_more'),
        ('transactions', '0013_alter_purchaseorder_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'permissions': (('can_undelete', 'Can undelete this object'),)},
        ),
        migrations.AddField(
            model_name='invoice',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True),
        ),
        migrations.CreateModel(
            name='HistoricalInvoice',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('sale', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='transactions.sale')),
            ],
            options={
                'verbose_name': 'historical invoice',
                'verbose_name_plural': 'historical invoices',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
