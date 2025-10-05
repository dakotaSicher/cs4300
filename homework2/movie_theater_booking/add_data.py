import os
import sys
import django
from datetime import datetime, timedelta

# Add the project directory to the Python path
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_dir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_theater_booking.settings')
django.setup()

# Now you can import your models
from bookings.models import Movie, Booking, Seat

# Create Movies
movies = [
    {
        'title': 'The Matrix Resurrections',
        'description': 'Return to the world of two realities in the latest Matrix installment',
        'release_date': datetime(2025, 10, 1),
        'duration': timedelta(hours=2, minutes=30)
    },
    {
        'title': 'Dune: Part Two',
        'description': 'The saga continues as Paul Atreides unites with the Fremen',
        'release_date': datetime(2025, 9, 15),
        'duration': timedelta(hours=2, minutes=45)
    },
    {
        'title': 'Avatar 3',
        'description': 'Return to Pandora in this third installment of the Avatar series',
        'release_date': datetime(2025, 11, 1),
        'duration': timedelta(hours=3)
    },
    {
        'title': 'Blade Runner 2099',
        'description': 'A new chapter in the Blade Runner saga',
        'release_date': datetime(2025, 9, 30),
        'duration': timedelta(hours=2, minutes=20)
    },
    {
        'title': 'Mission: Impossible 8',
        'description': 'Tom Cruise returns for another impossible mission',
        'release_date': datetime(2025, 10, 15),
        'duration': timedelta(hours=2, minutes=15)
    }
]

# Create the movies
for movie_data in movies:
    Movie.objects.create(**movie_data)
    
for i in range(1, 11):
    Seat.objects.create( number=i, status=True)

# Create a sample booking for a user
user_name = "John Doe"
movie = Movie.objects.first()  # Get the first movie
seat = Seat.objects.first()    # Get the first seat

# Create the booking
Booking.objects.create(
    movie=movie,
    seat=seat,
    user=user_name,
    book_date=datetime.now()
)




