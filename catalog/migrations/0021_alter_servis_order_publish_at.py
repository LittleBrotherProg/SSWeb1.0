# Generated by Django 3.2.4 on 2021-07-09 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0020_auto_20210709_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servis_order',
            name='publish_at',
            field=models.DateTimeField(help_text='Время обновления', null=True, verbose_name='Время обновления'),
        ),
    ]
