# Generated by Django 4.2.7 on 2023-11-14 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_create_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='create_date',
        ),
    ]