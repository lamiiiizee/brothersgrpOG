# Generated by Django 4.2.3 on 2023-08-24 14:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [('web', '0015_alter_update_summary_sectorfeature')]

    operations = [migrations.RemoveField(model_name='sectorfeature', name='icon')]