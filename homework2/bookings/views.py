from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, engines
from .models import Movie, Seat, Booking
from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import MovieSerializer,SeatSerializer,BookingSerializer

# Create your views here.

def movie_list(request):
    viewset = MovieViewSet()
    viewset.request = request
    movie_list = viewset.get_queryset()
    template = loader.get_template('movie_list.html')
    context = {
        'movies': movie_list,
    }
    return HttpResponse(template.render(context, request))

def seat_list(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    template = loader.get_template('book_seat.html')
    booked_seat_ids = Booking.objects.filter(movie=movie).values_list('seat_id', flat=True)
    seat_list = Seat.objects.all()
    for seat in seat_list:
        if seat.id in booked_seat_ids:
            seat.status = False

    context = {
        'seats': seat_list,
        'movie': movie,
    }
    return HttpResponse(template.render(context, request))

def book_seat(request, movie_id, seat_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seat = get_object_or_404(Seat, id=seat_id)

    Booking.objects.create(
        movie=movie,
        seat=seat,
        user="John Doe",
        book_date=datetime.now())

    # Create a simple template string with the base template and message
    template_string = """
    {% extends "base.html" %}
    {% block content %}
      <div class="container mt-4">
        <div class="alert alert-success" role="alert">
          Seat booked successfully for <strong>{{ movie.title }}</strong>!
        </div>
      </div>
    {% endblock %}
    """

    django_engine = engines['django']  # use the same engine Django uses normally
    template = django_engine.from_string(template_string)
    context = {'movie': movie}
    return HttpResponse(template.render(context, request))

def booking_history(request, username="John Doe"):
    bookings = Booking.objects.filter(user=username)
    template = loader.get_template('booking_history.html')
    context = {
        'bookings': bookings,  # This will include movie_title and seat_number
    }
    return HttpResponse(template.render(context, request))



class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    def get_queryset(self):
        movie_id = self.request.query_params.get('movie_id',None)
        queryset = Seat.objects.all()
        booked_seats = Booking.objects.filter(
            movie_id=movie_id
        ).values_list('seat_id', flat=True)
        for seat in queryset:
            if seat.id in booked_seats:
                seat.status = False

        return queryset
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_queryset(self):
        username = self.request.query_params.get('user', None)
        if username is not None:
            return Booking.objects.filter(user=username)
        return Booking.objects.all()

    def perform_create(self, serializer):
        seat = serializer.validated_data['seat']
        movie = serializer.validated_data['movie']

        if Booking.objects.filter(movie=movie, seat=seat).exists():
            raise serializers.ValidationError('This seat is already booked for this movie.')
        serializer.save()
    
