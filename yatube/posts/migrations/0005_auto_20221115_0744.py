# Generated by Django 2.2.16 on 2022-11-15 07:44

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20221115_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='posts/', verbose_name='Изображение'),
        ),
    ]
