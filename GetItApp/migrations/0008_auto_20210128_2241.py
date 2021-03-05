# Generated by Django 3.1.5 on 2021-01-28 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GetItApp', '0007_auto_20210128_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='important_information',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='information',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='is_technology',
            field=models.BooleanField(default=False),
        ),
    ]
