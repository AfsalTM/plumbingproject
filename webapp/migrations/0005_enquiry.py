# Generated by Django 5.1.2 on 2024-11-17 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_bookingdb_job_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bathrooms', models.IntegerField()),
                ('area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('request', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
