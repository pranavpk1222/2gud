# Generated by Django 5.0.2 on 2024-03-03 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0004_remove_imagemodel_product_id_productmodel_image_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='img_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
