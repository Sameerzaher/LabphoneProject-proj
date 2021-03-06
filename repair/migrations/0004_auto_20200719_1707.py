# Generated by Django 3.0.8 on 2020-07-19 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0003_auto_20200718_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='repair',
            name='brand',
            field=models.CharField(choices=[('Apple', 'Apple'), ('Samsung', 'Samsung'), ('Xioami', 'Xioami'), ('LG', 'LG')], default=1, max_length=70),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='repair',
            name='Device',
            field=models.CharField(choices=[('iPhone 11 Pro', 'iPhone 11 Pro'), ('Samsung Galaxy S20', 'Samsung Galaxy S20'), ('Samsung Galaxy Note 10+', 'Samsung Galaxy Note 10+'), ('Samsung Galaxy Note 10', 'Samsung Galaxy Note 10'), ('iPhone 11 Pro Max', 'iPhone 11 Pro Max'), ('iPhone 11', 'iPhone 11 '), ('Samsung Galaxy S20+', 'Samsung Galaxy S20+'), ('Samsung Galaxy S20 Ultra', 'Samsung Galaxy S20 Ultra')], max_length=70),
        ),
        migrations.AlterField(
            model_name='repair',
            name='bug',
            field=models.CharField(choices=[('Broken Screen', 'Broken Screen'), ('Broken Back', 'Broken Back'), ('Not Charging', 'Not Charging'), ('Broken', 'Broken'), ('Total Lost', 'Total Lost')], max_length=70),
        ),
    ]
