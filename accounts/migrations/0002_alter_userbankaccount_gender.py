# Generated by Django 5.0 on 2023-12-26 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbankaccount',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=50),
        ),
    ]
