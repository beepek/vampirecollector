from django.db import models
from django.urls import reverse

# Create your models here.


class Victim(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('victims_detail', kwargs={'pk': self.id})



class Bat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    victims = models.ManyToManyField(Victim)

    
    def get_absolute_url(self):

        return reverse('detail', kwargs={'bat_id': self.id})

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)        

class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
        )
    bat = models.ForeignKey(Bat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"   
    class Meta:
        ordering = ['-date']        