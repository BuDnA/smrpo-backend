# Generated by Django 2.0.3 on 2018-04-21 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20180420_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]