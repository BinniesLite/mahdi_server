# Generated by Django 4.1.7 on 2023-02-26 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.URLField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.URLField(default=None, null=True),
        ),
    ]
