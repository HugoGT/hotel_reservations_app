from json import loads

from django.views import View
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import viewsets

from .models import Reservation
# from .serializers import ReservationSerializer


class ReservationView(View):
    # queryset=Reservation.objects.all()
    # serializer_class=ReservationSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            reservations = list(Reservation.objects.filter(id=id).values())
            if len(reservations) > 0:
                reservation = reservations[0]
                data = {'message': 'Success', 'reservation': reservation,}
            else:
                data = {'message': 'Reservation not found'}

            return JsonResponse(data)
        else:
            reservations = list(Reservation.objects.values())
            if len(reservations)>0:
                data = {'message':'Success', 'reservations': reservations,}
            else:
                data = {'message':'Reservations not found'}

            return JsonResponse(data)

    def post(self, request):
        jd = loads(request.body)
        Reservation.objects.create(
            status=jd['status'],
            reserved_room=jd['reserved_room'],
            date_and_time_of_reservation=jd['date_and_time_of_reservation'],
            client_fullname=jd['client_fullname'],
            days_of_stay=jd['days_of_stay'],
            amount_paid=jd['amount_paid'],
            payment_method=jd['payment_method'],
            )

        data = {'message': 'Success',}

        return JsonResponse(data)

    def put(self, request, id):
        jd = loads(request.body)
        reservations = list(Reservation.objects.filter(id=id).values())
        if len(reservations) > 0:
            reservation = Reservation.objects.get(id=id)
            reservation.status=jd['status']
            reservation.reserved_room=jd['reserved_room']
            reservation.date_and_time_of_reservation=jd['date_and_time_of_reservation']
            reservation.client_fullname=jd['client_fullname']
            reservation.days_of_stay=jd['days_of_stay']
            reservation.amount_paid=jd['amount_paid']
            reservation.payment_method=jd['payment_method']
            reservation.save()
            data = {'message': 'Success'}
        else:
            data = {'message': 'Reservation not found'}

        return JsonResponse(data)

    def delete(self, request, id):
        jd = loads(request.body)
        reservations = list(Reservation.objects.filter(id=id).values())
        if len(reservations) > 0:
            reservation = Reservation.objects.get(id=id)
            jd['status'] = 'CANCELLED'
            jd['reserved_room'] = 'NONE'
            jd['date_and_time_of_reservation'] = '0001-01-01'
            jd['days_of_stay'] = 0
            jd['payment_method'] = 'NONE'
            reservation.status=jd['status']
            reservation.reserved_room=jd['reserved_room']
            reservation.date_and_time_of_reservation=jd['date_and_time_of_reservation']
            reservation.days_of_stay=jd['days_of_stay']
            reservation.payment_method=jd['payment_method']
            reservation.save()
            data = {'message': 'Success'}
        else:
            data = {'message': 'Reservation not found'}

        return JsonResponse(data)