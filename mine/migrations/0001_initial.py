# Generated by Django 3.2.1 on 2022-02-17 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('stone_type', models.CharField(max_length=255)),
                ('discovery_license_number', models.CharField(max_length=125)),
                ('date_of_issuance_of_the_discovery_license_number', models.DateField()),
                ('operating_license_number', models.CharField(max_length=125)),
                ('date_of_issuance_of_operating_license_number', models.DateField()),
                ('minimum_operating_tonnage', models.IntegerField()),
                ('government_law', models.IntegerField()),
                ('province', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('village', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/madan/')),
                ('description', models.TextField()),
                ('address', models.TextField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('long', models.FloatField(blank=True, null=True)),
                ('summary', models.TextField()),
                ('bold', models.TextField()),
                ('sub_bold', models.TextField()),
            ],
        ),
    ]
