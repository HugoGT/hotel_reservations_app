# Generated by Django 4.1 on 2022-08-25 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_reservation_client_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='client_fullname',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='days_of_stay',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='payment_method',
            field=models.CharField(choices=[('CASH', 'Cash'), ('CARD', 'Card'), ('PAYPAL', 'Paypal'), ('BANK_TRANSFER', 'Bank transfer')], default='CASH', max_length=16),
        ),
    ]
