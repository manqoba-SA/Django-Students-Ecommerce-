# Generated by Django 3.1.5 on 2021-01-27 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GetItApp', '0002_auto_20210126_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='categories'),
        ),
    ]
