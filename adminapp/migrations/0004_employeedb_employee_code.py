# Generated by Django 5.1.2 on 2024-11-13 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_servicedb_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedb',
            name='employee_code',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
