# Generated by Django 4.2.3 on 2023-08-15 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_system', '0014_goods_received_project_type_project_type_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods_received',
            name='remaining',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]