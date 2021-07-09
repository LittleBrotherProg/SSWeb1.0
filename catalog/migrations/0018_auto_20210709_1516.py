# Generated by Django 3.2.4 on 2021-07-09 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_auto_20210709_1513'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servis_order',
            options={'ordering': ('created_at',), 'verbose_name': 'Заказы', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.RenameField(
            model_name='servis_order',
            old_name='date',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='servis_order',
            name='publish_at',
            field=models.DateField(blank=True, help_text='Дата заказа', null=True, verbose_name='Дата'),
        ),
    ]
