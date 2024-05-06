# Generated by Django 5.0.2 on 2024-02-27 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddressModel',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
                ('alternative_phone_number', models.CharField(max_length=10)),
                ('landmark', models.CharField(max_length=50)),
                ('pin_code', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'user_address_table',
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'user_details',
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('order_date', models.DateTimeField(auto_created=True)),
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.CharField(max_length=10)),
                ('spec_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.specificationmodel')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.useraddressmodel')),
            ],
            options={
                'db_table': 'oder_table',
            },
        ),
        migrations.CreateModel(
            name='FeedbackModel',
            fields=[
                ('feedback_date', models.DateTimeField(auto_created=True)),
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('feedback_text', models.CharField(max_length=600)),
                ('oder_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.ordermodel')),
            ],
            options={
                'db_table': 'feedback_table',
            },
        ),
        migrations.AddField(
            model_name='useraddressmodel',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.usermodel'),
        ),
        migrations.CreateModel(
            name='FavouriteModel',
            fields=[
                ('favorite_id', models.AutoField(primary_key=True, serialize=False)),
                ('spec_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.specificationmodel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.usermodel')),
            ],
            options={
                'db_table': 'favourite_table',
            },
        ),
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('create_at', models.DateTimeField(auto_created=True)),
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('spec_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.specificationmodel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.usermodel')),
            ],
            options={
                'db_table': 'cart_table',
            },
        ),
    ]
