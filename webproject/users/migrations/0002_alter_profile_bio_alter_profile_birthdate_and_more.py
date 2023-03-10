# Generated by Django 4.1.5 on 2023-02-09 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='external_link',
            field=models.URLField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook_link',
            field=models.URLField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.jpeg', upload_to='profile.pics'),
        ),
    ]
