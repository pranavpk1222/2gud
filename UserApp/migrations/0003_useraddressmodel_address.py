# Generated by Django 5.0.2 on 2024-03-13 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_useraddressmodel_address_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddressmodel',
            name='address',
            field=models.CharField(max_length=300, null=True),
        ),
    ]