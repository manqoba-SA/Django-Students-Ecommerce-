# Generated by Django 3.1.5 on 2021-02-02 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='building',
            field=models.CharField(choices=[('Quantile', 'Quantile'), ('Herb Str', 'Herb Str'), ('Minller Str', 'Minller Str')], max_length=100),
        ),
    ]
