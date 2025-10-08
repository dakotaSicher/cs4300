#chat gpt

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from datetime import datetime, timedelta
from bookings.models import Movie, Seat, Booking

class ModelTests(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Inception",
            description="Dreams within dreams",
            release_date=datetime(2010, 7, 16),
            duration=timedelta(minutes=148)
        )
        self.seat = Seat.objects.create(number=1)

    def test_movie_str(self):
        self.assertEqual(str(self.movie), "Inception")

    def test_seat_str(self):
        self.assertEqual(str(self.seat), "Seat 1")

    def test_create_booking(self):
        booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user="John Doe",
            book_date=datetime.now()
        )
        self.assertEqual(booking.movie.title, "Inception")
        self.assertEqual(booking.seat.number, 1)


class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.create(
            title="Interstellar",
            description="Space exploration",
            release_date=datetime(2014, 11, 7),
            duration=timedelta(minutes=169)
        )
        self.seat = Seat.objects.create(number=7)

    def test_list_movies(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_list_seats(self):
        response = self.client.get('/api/seats/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_booking(self):
        data = {
            'movie': self.movie.id,
            'seat': self.seat.id,
            'user': 'Test User',
            'book_date': datetime.now().isoformat()
        }
        response = self.client.post('/api/bookings/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)

    def test_booking_conflict(self):
        # First booking succeeds
        Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user='Test User',
            book_date=datetime.now()
        )
        # Second booking on same seat should fail
        data = {
            'movie': self.movie.id,
            'seat': self.seat.id,
            'user': 'Another User',
            'book_date': datetime.now().isoformat()
        }
        response = self.client.post('/api/bookings/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)