# Generated by Django 3.1 on 2022-04-30 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220414_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Esewa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_key', models.CharField(blank=True, default='epay_payment', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Khalti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_key', models.CharField(blank=True, default='', max_length=200)),
                ('private_key', models.CharField(blank=True, default='', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='usersetting',
            name='verification_expires',
            field=models.DateField(default=datetime.date(2022, 5, 3)),
        ),
    ]