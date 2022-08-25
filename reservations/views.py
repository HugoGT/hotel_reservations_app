from json import loads

from django.views import View
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet

from .models import Reservation
from .serializers import ReservationSerializer


class ReservationView(ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            reservations = list(Reservation.objects.filter(id=id).values())
            if len(reservations) > 0:
                reservation = reservations[0]
                response = {'message': 'Success', 'reservation': reservation,}
            else:
                response = {'message': 'Reservation not found'}

            return JsonResponse(response)
        else:
            reservations = list(Reservation.objects.values())
            if len(reservations)>0:
                response = {'message':'Success', 'reservations': reservations,}
            else:
                response = {'message':'Reservations not found'}

            return JsonResponse(response)

    def post(self, request):
        data = loads(request.body)
        Reservation.objects.create(
            status=data['status'],
            reserved_room=data['reserved_room'],
            date_and_time_of_reservation=data['date_and_time_of_reservation'],
            client_fullname=data['client_fullname'],
            days_of_stay=data['days_of_stay'],
            amount_paid=data['amount_paid'],
            payment_method=data['payment_method'],
            )

        response = {'message': 'Success',}

        return JsonResponse(response)

    def put(self, request, id):
        data = loads(request.body)
        reservations = list(Reservation.objects.filter(id=id).values())
        if len(reservations) > 0:
            reservation = Reservation.objects.get(id=id)
            reservation.status=data['status']
            reservation.reserved_room=data['reserved_room']
            reservation.date_and_time_of_reservation=data['date_and_time_of_reservation']
            reservation.client_fullname=data['client_fullname']
            reservation.days_of_stay=data['days_of_stay']
            reservation.amount_paid=data['amount_paid']
            reservation.payment_method=data['payment_method']
            reservation.save()
            response = {'message': 'Success'}
        else:
            response = {'message': 'Reservation not found'}

        return JsonResponse(response)

    def delete(self, request, id):
        reservations = list(Reservation.objects.filter(id=id).values())
        if len(reservations) > 0:
            Reservation.objects.get(id=id).delete()
            data = {'message': 'Success'}
        else:
            data = {'message': 'Reservation not found'}

        return JsonResponse(data)