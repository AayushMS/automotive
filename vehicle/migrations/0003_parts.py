# Generated by Django 4.1.4 on 2022-12-29 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_rename_manufactured_data_vehicle_manufactured_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('manufactuer', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
