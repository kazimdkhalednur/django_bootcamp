# Generated by Django 4.2.7 on 2023-11-20 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_book_updated_at_alter_book_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book2',
            fields=[
                ('id', models.UUIDField(blank=True, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
