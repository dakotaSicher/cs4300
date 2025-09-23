from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    release_data = models.DateTimeField("release data")
    duration = models.DurationField("movie lenght")

class Seat(models.Model):
    number = models.IntegerField("Seat Number")
    status = models.BooleanField("available", default = True)

class Booking(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat,on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    book_date = models.DateTimeField("date of booking")