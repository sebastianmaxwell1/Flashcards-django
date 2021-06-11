from django.db import models


class Flashcard(models.Model):
    question = models.CharField(max_length=50, default=None)
    answer = models.CharField(max_length=50, null=True)
    collection= models.ForeignKey('flashcards.Collection', default=None, null=True, on_delete=models.CASCADE)

class Collection(models.Model):
    title = models.CharField(max_length=50)


