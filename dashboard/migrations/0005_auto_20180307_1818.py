# Generated by Django 2.0.1 on 2018-03-07 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20180118_1711'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='associate',
            options={},
        ),
        migrations.AlterField(
            model_name='refund',
            name='order_date',
            field=models.DateField(blank=True, max_length=50, null=True, verbose_name='거래날짜'),
        ),
        migrations.AlterField(
            model_name='refund',
            name='order_number',
            field=models.CharField(max_length=50, null=True, verbose_name='온라인주문번호'),
        ),
    ]
