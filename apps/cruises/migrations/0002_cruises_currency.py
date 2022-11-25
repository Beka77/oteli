# Generated by Django 4.1 on 2022-11-22 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_alter_contact_status_contact'),
        ('cruises', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cruises',
            name='currency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cruises_currency', to='settings.currency'),
            preserve_default=False,
        ),
    ]
