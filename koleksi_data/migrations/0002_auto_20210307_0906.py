# Generated by Django 3.1.7 on 2021-03-07 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koleksi_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rekaman',
            old_name='user_id',
            new_name='user',
        ),
    ]