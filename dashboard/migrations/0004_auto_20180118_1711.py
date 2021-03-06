# Generated by Django 2.0.1 on 2018-01-18 08:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20180118_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='refund',
            name='last_edited_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='최종수정일'),
        ),
        migrations.AddField(
            model_name='refund',
            name='order_date',
            field=models.DateTimeField(blank=True, max_length=50, null=True, verbose_name='매장거래일'),
        ),
        migrations.AlterField(
            model_name='refund',
            name='note',
            field=models.TextField(blank=True, verbose_name='사유 및 내용'),
        ),
        migrations.AlterField(
            model_name='refund',
            name='order_number',
            field=models.CharField(blank=True, max_length=50, verbose_name='온라인주문번호'),
        ),
    ]
