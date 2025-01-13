# Generated by Django 5.1.4 on 2025-01-05 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0002_chatmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='LLMModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('model_type', models.CharField(choices=[('llama', 'Llama'), ('openai', 'OpenAI')], max_length=10)),
                ('path', models.CharField(blank=True, max_length=255, null=True)),
                ('openai_model_id', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]