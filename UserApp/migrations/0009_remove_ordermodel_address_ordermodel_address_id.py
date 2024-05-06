# Generated by Django 5.0.2 on 2024-03-15 10:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0008_alter_ordermodel_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='address',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='address_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UserApp.useraddressmodel'),
        ),
    ]
