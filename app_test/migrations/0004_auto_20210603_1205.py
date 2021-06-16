# Generated by Django 3.2.4 on 2021-06-03 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_test', '0003_auto_20210603_1205'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='testmodel',
            name='unique quittance',
        ),
        migrations.AddConstraint(
            model_name='testmodel',
            constraint=models.UniqueConstraint(fields=('name', 'apartment_id'), name='unique name-apartment'),
        ),
    ]