# Generated by Django 4.2.7 on 2023-11-13 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_book_discount_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='discount_price',
            field=models.DecimalField(decimal_places=2, default='456', max_digits=5),
        ),
    ]
