from django.db import models

class Novel(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    published_date = models.DateField()
    synopsis = models.TextField()

    def __str__(self):
        return self.title
