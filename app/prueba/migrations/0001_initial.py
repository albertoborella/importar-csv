# Generated by Django 4.1 on 2023-07-24 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('latitud', models.CharField(blank=True, max_length=100, null=True)),
                ('longitud', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.URLField()),
                ('tipo_propiedad', models.CharField(blank=True, max_length=100, null=True)),
                ('precio', models.CharField(blank=True, max_length=100, null=True)),
                ('moneda', models.CharField(blank=True, max_length=100, null=True)),
                ('m2', models.CharField(blank=True, max_length=100, null=True)),
                ('ambientes', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
