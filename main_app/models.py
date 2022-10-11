from django.db import models
from datetime import date

# Celeb Model 
class Celeb(models.Model):
    name = models.CharField(max_length=250)
    image = models.CharField(max_length=500)
    bio = models.CharField(max_length=500)
    created_at= models.DateTimeField(auto_now_add=True)
    coverphoto = models.CharField(max_length=1000, default='')

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
    celeb = models.ManyToManyField(Celeb)

    def __str__(self):
        return self.title

class BlindItem(models.Model):
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=1000)
    date_posted = models.DateField(default=date.today)
    celeb = models.ManyToManyField(Celeb)

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=300)
    summary = models.CharField(max_length=500)
    url = models.CharField(max_length=1000, default='')
    cover_photo = models.CharField(max_length=1000, default='')
    date_posted =models.DateField(default=date.today)
    celeb = models.ManyToManyField(Celeb)

    def __str__(self):
        return self.title 

class Video(models.Model):
    video = models.CharField(max_length=900)
    thumbnail= models.CharField(max_length=900, default='')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date_taken = models.DateField(default=date.today)
    celeb = models.ManyToManyField(Celeb)

    def __str__(self):
        return self.title

class MessageBoard(models.Model):
    title = models.CharField(max_length=300)
    body = models.CharField(max_length=1000)
    date_posted = models.DateField(default=date.today)
    celeb = models.ManyToManyField(Celeb)

    def _str_(self):
        return self.title
    
# Comment Models 

class PhotoComments(models.Model):
    username = models.CharField(max_length=100, default='')
    body = models.CharField(max_length=1000)
    date_posted = models.DateField(default=date.today)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.body

class VideoComment(models.Model):
    username = models.CharField(max_length=100, default='')
    body = models.CharField(max_length=1000)
    date_posted = models.DateField(default=date.today)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.body


class BlindItemComment(models.Model):
    username = models.CharField(max_length=100, default='')
    body = models.CharField(max_length=1000)
    date_posted = models.DateField(default=date.today)
    blind = models.ForeignKey(BlindItem, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.body

class ArticleComment(models.Model):
    username = models.CharField(max_length=100, default='')
    body = models.CharField(max_length=1000)
    date_posted = models.DateField(default=date.today)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.body

class MessageBoardComment(models.Model):
    username = models.CharField(max_length=100, default='')
    body = models.CharField(max_length=1000)
    date_posted = models.DateField(default=date.today)
    messageboard = models.ForeignKey(MessageBoard, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.body