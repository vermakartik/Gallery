# Generated by Django 2.1.5 on 2019-01-08 15:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_gallery', '0003_auto_20190108_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
