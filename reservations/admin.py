from django.contrib import admin

from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'status',
        'reserved_room',
        'date_and_time_of_reservation',
        'client_fullname',
        'days_of_stay',
        'amount_paid',
        'payment_method'
        ]
