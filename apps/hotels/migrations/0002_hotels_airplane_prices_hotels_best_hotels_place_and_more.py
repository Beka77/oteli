# Generated by Django 4.1 on 2022-11-19 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='airplane_prices',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotels',
            name='best',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hotels',
            name='place',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotels',
            name='sale',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
