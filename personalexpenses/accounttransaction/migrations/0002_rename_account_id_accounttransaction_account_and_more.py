# Generated by Django 4.2.19 on 2025-03-05 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounttransaction', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounttransaction',
            old_name='account_id',
            new_name='account',
        ),
        migrations.RenameField(
            model_name='accounttransaction',
            old_name='user_id',
            new_name='user',
        ),
    ]
