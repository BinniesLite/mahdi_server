# Generated by Django 4.1.7 on 2023-02-26 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_image_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]
