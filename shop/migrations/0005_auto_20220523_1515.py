# Generated by Django 3.1 on 2022-05-23 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_khalti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash On Delivery', 'Cash On Delivery'), ('Esewa', 'Esewa'), ('Khalti', 'Khalti'), ('Google_Pay', 'Google_Pay')], default='Cash On Delivery', max_length=20),
        ),
    ]
