# Generated by Django 5.1.4 on 2024-12-31 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='votes_total',
            field=models.IntegerField(default=0),
        ),
    ]