# Generated by Django 5.1 on 2024-08-23 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_catagory_options_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.RemoveField(
            model_name='item',
            name='created_by',
        ),
        migrations.DeleteModel(
            name='Catagory',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
