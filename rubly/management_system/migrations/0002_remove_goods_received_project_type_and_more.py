# Generated by Django 4.2.3 on 2023-08-24 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management_system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods_received',
            name='Project_Type',
        ),
        migrations.AlterUniqueTogether(
            name='purchase_order',
            unique_together={('purchase_ID', 'project_type')},
        ),
    ]