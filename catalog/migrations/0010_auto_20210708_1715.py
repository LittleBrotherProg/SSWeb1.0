# Generated by Django 3.2.4 on 2021-07-08 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_rename_cust_servis_order_заказчик'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servis_order',
            old_name='date',
            new_name='Дата',
        ),
        migrations.RenameField(
            model_name='servis_order',
            old_name='заказчик',
            new_name='Заказчик',
        ),
        migrations.RenameField(
            model_name='servis_order',
            old_name='status',
            new_name='Статус',
        ),
        migrations.RenameField(
            model_name='servis_order',
            old_name='Services',
            new_name='Услуга',
        ),
    ]
