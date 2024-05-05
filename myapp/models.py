from django.db import models

class Ztest(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

