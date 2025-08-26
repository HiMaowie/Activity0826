from django.db import models
from django.conf import settings


class History(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    method = models.CharField(max_length=10)
    tweet = models.ForeignKey('tweet.Tweet', on_delete=models.CASCADE)
    date = models.DateTimeField()
    summary = models.TextField()


    def __str__(self):
        return f"{self.method} by {self.user.username} on {self.date}"