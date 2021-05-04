from django.db import models


class FlashcardFront(models.Model):
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=50, null=True)
    card_number = models.IntegerField(blank=True, null=True)



# Create your models here.
