# Generated by Django 3.2.4 on 2021-06-30 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20210630_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='servis_order',
            name='status',
            field=models.CharField(blank=True, choices=[('Н', 'Новый'), ('Р', 'В работе'), ('В', 'Выполнен')], default='Н', help_text='Статус заказа', max_length=1),
        ),
    ]
