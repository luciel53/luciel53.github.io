# Generated by Django 4.1.5 on 2023-02-16 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('breed', '0013_annimal_post_flaws_annimal_post_qualities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annimal_post',
            name='flaws',
        ),
        migrations.RemoveField(
            model_name='annimal_post',
            name='qualities',
        ),
    ]
