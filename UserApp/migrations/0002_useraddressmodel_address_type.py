# Generated by Django 5.0.2 on 2024-03-13 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddressmodel',
            name='address_type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
