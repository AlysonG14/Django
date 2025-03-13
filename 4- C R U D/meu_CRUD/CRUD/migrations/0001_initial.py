# Generated by Django 5.1.7 on 2025-03-13 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('título', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('ano_publicacao', models.DateField(auto_now=True)),
                ('informacoes', models.CharField(max_length=500)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
