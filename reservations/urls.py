from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ReservationView

router = DefaultRouter()
router.register(prefix='reservations', basename='reservations', viewset=ReservationView)


urlpatterns = [
    path('hotel-app/', include(router.urls), name='reservations_list'),
    path('hotel-app/<int:id>', include(router.urls), name='reservation_process'),
]