# Generated by Django 5.1.2 on 2024-10-31 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplicationdb',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
