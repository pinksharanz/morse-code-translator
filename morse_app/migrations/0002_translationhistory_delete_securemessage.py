# Generated by Django 5.1.6 on 2025-03-13 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morse_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TranslationHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_text', models.TextField()),
                ('morse_output', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='SecureMessage',
        ),
    ]
