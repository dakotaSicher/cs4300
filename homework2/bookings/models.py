from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    release_date = models.DateTimeField("release date")
    duration = models.DurationField("movie length")

    def __str__(self):
        return self.title

class Seat(models.Model):
    number = models.IntegerField("Seat Number")
    status = models.BooleanField("available", default = True)

    def __str__(self):
        return "Seat " + str(self.number)

class Booking(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat,on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    book_date = models.DateTimeField("date of booking")
