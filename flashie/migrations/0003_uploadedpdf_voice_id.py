# Generated by Django 5.1.4 on 2025-01-19 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashie', '0002_alter_uploadedpdf_audio_alter_uploadedpdf_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedpdf',
            name='voice_id',
            field=models.CharField(default='Joanna', max_length=50),
        ),
    ]