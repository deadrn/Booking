from django.db import models
from django.forms.fields import FloatField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title
#Room
class Room(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    price = FloatField()
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"room №{self.number} for {self.capacity} person(s)"

#Booking model
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked room №{self.room.number} from {self.start_date} to {self.end_date}"


    