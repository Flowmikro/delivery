# Generated by Django 3.2.16 on 2023-05-25 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TruckModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('load_capacity', models.PositiveSmallIntegerField()),
                ('sku', models.CharField(blank=True, max_length=5, unique=True)),
                ('zip', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state_name', models.CharField(blank=True, max_length=255, null=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('lng', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
            ],
        ),
    ]
