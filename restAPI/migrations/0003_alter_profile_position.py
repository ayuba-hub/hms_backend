# Generated by Django 4.0.2 on 2022-04-24 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0002_alter_profile_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('cashier', 'Cashier'), ('receptionist', 'Receptionist'), ('admin', 'Admin')], default='', max_length=100),
        ),
    ]
