# Generated by Django 4.2.3 on 2023-08-03 08:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=50)),
                ('Type', models.CharField(max_length=50)),
                ('Packaging', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_ID', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Returns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('Quantity', models.IntegerField()),
                ('returned_by', models.CharField(max_length=50)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_system.description')),
            ],
        ),
        migrations.CreateModel(
            name='IssuanceInternal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('issuedTo', models.CharField(max_length=50)),
                ('Project', models.CharField(max_length=50)),
                ('Quantity', models.IntegerField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_system.description')),
            ],
        ),
        migrations.CreateModel(
            name='IssuanceExternal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=50)),
                ('Carpex', models.CharField(max_length=50)),
                ('Quantity', models.IntegerField()),
                ('Purchase_order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management_system.purchase_order')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_system.description')),
            ],
        ),
        migrations.CreateModel(
            name='Checkin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('Description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_system.description')),
                ('Purchase_Order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management_system.purchase_order')),
                ('Warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_system.warehouse')),
            ],
        ),
    ]
