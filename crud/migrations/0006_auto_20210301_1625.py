# Generated by Django 3.1.6 on 2021-03-01 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_auto_20210301_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cityleadership',
            name='bitrhday',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='countryleadership',
            name='bitrhday',
            field=models.DateTimeField(),
        ),
    ]
