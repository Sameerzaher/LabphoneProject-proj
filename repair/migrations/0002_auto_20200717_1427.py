# Generated by Django 3.0.8 on 2020-07-17 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repair',
            old_name='title',
            new_name='Device',
        ),
    ]