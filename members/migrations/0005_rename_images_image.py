# Generated by Django 4.1.7 on 2023-03-02 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_images'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
    ]
