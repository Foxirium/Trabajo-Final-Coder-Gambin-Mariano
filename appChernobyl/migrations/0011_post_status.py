# Generated by Django 4.0.4 on 2022-05-19 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appChernobyl', '0010_remove_post_autor_post_author_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Publish/Not Publish'),
        ),
    ]