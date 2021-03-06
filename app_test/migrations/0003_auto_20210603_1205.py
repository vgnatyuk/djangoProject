# Generated by Django 3.2.4 on 2021-06-03 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_test', '0002_alter_testmodel_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='testmodel',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='testmodel',
            constraint=models.UniqueConstraint(fields=('name', 'apartment_id'), name='unique quittance'),
        ),
    ]
