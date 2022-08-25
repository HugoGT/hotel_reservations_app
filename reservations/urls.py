from django.urls import path, include

from rest_framework import routers

from .views import ReservationView

# router = routers.DefaultRouter()
# router.register('reservation', ReservationView)

#include(router.urls)

urlpatterns = [
    path('reservations/', ReservationView.as_view(), name='reservations_list'),
    path('reservations/<int:id>', ReservationView.as_view(), name='reservation_process'),
]