from rest_framework.serializers import ModelSerializer

from .models import Reservation

class ReservationSerializer(ModelSerializer):
    class Meta:
        model=Reservation
        fields=[
            'id',
            'status',
            'reserved_room',
            'date_and_time_of_reservation',
            'client_fullname',
            'days_of_stay',
            'amount_paid',
            'payment_method'
            ]