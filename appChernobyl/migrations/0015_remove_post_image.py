# Generated by Django 4.0.4 on 2022-05-20 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appChernobyl', '0014_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
