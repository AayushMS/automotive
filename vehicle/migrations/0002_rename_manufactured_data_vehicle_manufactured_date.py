# Generated by Django 4.1.4 on 2022-12-21 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='manufactured_data',
            new_name='manufactured_date',
        ),
    ]
