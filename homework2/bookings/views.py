from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, engines
from .models import Movie, Seat, Booking
from rest_framework import viewsets, status
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
    # Use BookingViewSet to get the bookings
    booking_viewset = BookingViewSet()
    booking_viewset.request = request
    # Add username as a query parameter
    booking_viewset.request.query_params = {'user': username}
    
    # Get bookings through the viewset
    bookings = booking_viewset.get_queryset()
    
    # Use the serializer to get readable data
    serializer = BookingSerializer(bookings, many=True)
    
    template = loader.get_template('booking_history.html')
    context = {
        'bookings': serializer.data,  # This will include movie_title and seat_number
    }
    return HttpResponse(template.render(context, request))



class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    http_method_names = ['get']
    
    def list(self,request):
        serializer = self.get_serializer()
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        movie = get_object_or_404(self.queryset, pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)



class SeatViewSet(viewsets.ModelViewSet):

    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    http_method_names = ['get']

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
    http_method_names = ['get','post']

    def get_queryset(self):
        queryset = Booking.objects.all()
        # Filter bookings by user if username is provided
        username = self.request.query_params.get('user', None)
        if username is not None:
            queryset = queryset.filter(user=username)
        return queryset

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            seat = serializer.validated_data['seat_id']
            movie = serializer.validated_data['movie_id']
            booked = Booking.objects.filter(movie_id=movie).values_list('seat_id', flat=True)
            if seat in booked:
                return Response(
                    {'error': 'This seat is already booked for this movie.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            serializer.validated_data['seat_id'].status = False
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)