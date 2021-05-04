from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile

# Create your models here.

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    title = models.CharField(max_length=30)
    content = models.TextField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                             related_name='comments', 
                             related_query_name='comment')
    created = models.DateField()
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)

    def __str__(self):
        return self.title
