
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# API routes
router = DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'seats', views.SeatViewSet)
router.register(r'booking_history', views.BookingViewSet)

# Combine API and template URLs
urlpatterns = [
    # Template views
    path('', views.movie_list, name='movie_list'),
    path('seat_list/<int:movie_id>', views.seat_list, name='seat_list'),
    path('book_seat/<int:movie_id>/<int:seat_id>/', views.book_seat, name='book_seat'),
    path('booking_history/',views.booking_history,name = 'booking_history'),
    # Include all API endpoints under 'api/'
    path('api/', include(router.urls)),
]
