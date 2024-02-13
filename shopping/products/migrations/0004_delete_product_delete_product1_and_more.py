# Generated by Django 5.0.1 on 2024-02-02 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='product',
        ),
        migrations.DeleteModel(
            name='product1',
        ),
        migrations.RemoveField(
            model_name='product2',
            name='description',
        ),
        migrations.AlterField(
            model_name='product2',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]