# Generated by Django 4.2.3 on 2023-08-24 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [('web', '0014_alter_sector_summary')]

    operations = [
        migrations.AlterField(model_name='update', name='summary', field=models.TextField(blank=True, null=True)),
        migrations.CreateModel(
            name='SectorFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                (
                    'sector',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='web.sector', verbose_name='Sector'
                    ),
                ),
            ],
        ),
    ]
