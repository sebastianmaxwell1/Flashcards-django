from django.db import models


class FlashcardFront(models.Model):
    question = models.CharField(max_length=50)
    card_number = models.IntegerField(blank=True, null=True)


# Create your models here.
