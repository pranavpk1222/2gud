# Generated by Django 5.0.2 on 2024-03-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0003_useraddressmodel_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='quantity',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
