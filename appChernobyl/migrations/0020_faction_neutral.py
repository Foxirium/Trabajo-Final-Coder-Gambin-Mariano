# Generated by Django 4.0.4 on 2022-05-22 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appChernobyl', '0019_faction_delete_factions'),
    ]

    operations = [
        migrations.AddField(
            model_name='faction',
            name='neutral',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
