# Generated by Django 3.1.5 on 2021-01-28 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GetItApp', '0006_auto_20210128_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.CharField(choices=[('per item', 'per item'), ('per packet', 'per packet'), ('per plastic', 'per plastic')], max_length=100),
        ),
    ]