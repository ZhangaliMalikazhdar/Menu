# Generated by Django 4.0.2 on 2022-03-20 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_maincategories_is_published_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maincategories',
            old_name='upload',
            new_name='picture',
        ),
    ]
