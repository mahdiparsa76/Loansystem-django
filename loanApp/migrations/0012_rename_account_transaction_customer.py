# Generated by Django 4.0.2 on 2022-07-14 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loanApp', '0011_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='account',
            new_name='customer',
        ),
    ]