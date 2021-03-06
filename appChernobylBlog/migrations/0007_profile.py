# Generated by Django 4.0.4 on 2022-06-03 18:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appChernobylBlog', '0006_post_abstract_post_image_alter_post_body_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('biography', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
