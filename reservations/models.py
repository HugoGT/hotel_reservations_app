from django.db import models
from django.utils import timezone


class Reservation(models.Model):
    status = models.CharField(
        max_length=10,
        choices=[('PENDING','Pending'), ('PAID','Paid'), ('CANCELLED','Cancelled')],
        default='PENDING',
    )

    reserved_room = models.CharField(
        max_length=8,
        choices=[('CLASSIC','Classic'), ('DOUBLE','Double'), ('SUITE','Suite')],
        default='CLASSIC'
    )

    date_and_time_of_reservation = models.DateField(
        default=timezone.now
    )

    client_fullname = models.CharField(
        max_length=80,
        default='',
    )

    days_of_stay = models.PositiveIntegerField(default=1)

    amount_paid = models.PositiveIntegerField(default=0)

    payment_method = models.CharField(
        max_length=16,
        choices=[('CASH','Cash'), ('CARD','Card'), ('PAYPAL','Paypal'), ('BANK_TRANSFER','Bank transfer')],
        default='CASH'
    )
