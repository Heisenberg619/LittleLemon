# Generated by Django 5.1.1 on 2024-10-11 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_rename_bookingtable_booking_rename_menutable_menu'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu',
            new_name='MenuItem',
        ),
    ]
