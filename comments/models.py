from django.db import models


class Comment(models.Model):

    message = models.CharField(max_length=1000)
