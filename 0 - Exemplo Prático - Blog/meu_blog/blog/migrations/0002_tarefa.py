# Generated by Django 5.1.6 on 2025-02-13 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrição', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('data_criacao1', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
