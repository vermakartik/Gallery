# Generated by Django 2.1.5 on 2019-01-10 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_gallery', '0006_auto_20190108_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image_file',
            field=models.ImageField(upload_to='documents/%Y/%m/%d/'),
        ),
    ]
