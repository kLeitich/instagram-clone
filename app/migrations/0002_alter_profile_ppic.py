# Generated by Django 4.0.5 on 2022-06-09 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ppic',
            field=models.ImageField(upload_to='ppic'),
        ),
    ]