# Generated by Django 4.0.4 on 2022-05-19 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appChernobyl', '0007_alter_blog_body'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='Post',
        ),
    ]