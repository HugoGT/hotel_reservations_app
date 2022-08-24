# Generated by Django 4.1 on 2022-08-24 20:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('PAID', 'Paid'), ('DELETED', 'Deleted')], default='PENDING', max_length=8)),
                ('reserved_room', models.CharField(choices=[('CLASSIC', 'Classic'), ('DOUBLE', 'Double'), ('SUITE', 'Suite')], default='CLASSIC', max_length=8)),
                ('date_and_time_of_reservation', models.DateField(default=django.utils.timezone.now)),
                ('days_of_stay', models.PositiveIntegerField()),
                ('amount_paid', models.PositiveIntegerField(default=0)),
                ('payment_method', models.CharField(choices=[('CASH', 'Cash'), ('CARD', 'Card'), ('PAYPAL', 'Paypal'), ('BANK_TRANSFER', 'Bank transfer')], max_length=16)),
            ],
        ),
    ]