# Generated by Django 5.0 on 2024-01-13 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_site_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapingTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_ids', models.TextField()),
            ],
        ),
    ]
