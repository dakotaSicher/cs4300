
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet, basename='movies')
router.register(r'seats', views.SeatViewSet,basename='seats')
router.register(r'bookings', views.BookingViewSet,basename='bookings')

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('seat_list/<int:movie_id>', views.seat_list, name='seat_list'),
    path('book_seat/<int:movie_id>/<int:seat_id>/', views.book_seat, name='book_seat'),
    path('booking_history/',views.booking_history,name = 'booking_history'),
    path('api/', include(router.urls)),
]
