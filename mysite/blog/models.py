from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=130)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        self.title




