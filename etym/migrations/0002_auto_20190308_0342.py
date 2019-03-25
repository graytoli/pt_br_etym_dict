# Generated by Django 2.0.13 on 2019-03-08 03:42

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):
    atomic = False
    
    dependencies = [
        ('etym', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Original',
            new_name='Origin',
        ),
        migrations.RenameField(
            model_name='modern',
            old_name='origin_language',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='modern',
            old_name='origin_word',
            new_name='origin',
        ),
        migrations.RenameField(
            model_name='modern',
            old_name='origin_region',
            new_name='region',
        ),
        migrations.RenameField(
            model_name='origin',
            old_name='origin_meaning',
            new_name='meaning',
        ),
        migrations.RenameField(
            model_name='origin',
            old_name='origin_word',
            new_name='word',
        ),
        migrations.AddField(
            model_name='region',
            name='address',
            field=django_google_maps.fields.AddressField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='region',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
