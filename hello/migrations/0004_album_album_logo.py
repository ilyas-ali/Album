# Generated by Django 3.0.7 on 2020-06-14 12:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_remove_album_album_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_logo',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
