# Generated by Django 5.1.6 on 2025-03-06 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ecommerce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='produtos/')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
