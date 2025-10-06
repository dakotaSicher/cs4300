from rest_framework import serializers
from .models import Movie, Seat, Booking

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','title','description','release_date','duration' ]


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id','number','status']
        

class BookingSerializer(serializers.ModelSerializer):
    #movie_title = serializers.CharField(source='movie.title', read_only=True)
    #seat_number = serializers.CharField(source='seat.number', read_only=True)
    
    class Meta:
        model = Booking
        fields = ['id', 'movie', 'seat', 'user', 'book_date']

