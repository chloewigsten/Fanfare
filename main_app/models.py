from django.db import models
from datetime import date

# Celeb Model 
class Celeb(models.Model):
    name = models.CharField(max_length=250)
    image = models.CharField(max_length=500)
    bio = models.CharField(max_length=500)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta: 
        ordering = ['name']

# Photos Model
class Photo(models.Model):
    photo = models.CharField(max_length=900)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date_taken = models.DateField(default=date.today)
    celebs = models.ForeignKey(Celeb, on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return self.photo

class BlindItem(models.Model):
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=1000)
    date_posted = models.DateField(default=date.today)
    celebs = models.ForeignKey(Celeb, on_delete=models.CASCADE, related_name='blind')

    def __str__(self):
        return self.title