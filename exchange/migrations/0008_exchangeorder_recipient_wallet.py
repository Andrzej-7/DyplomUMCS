# Generated by Django 4.2.7 on 2023-11-08 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0007_remove_exchangeorder_recipient_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchangeorder',
            name='recipient_wallet',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
