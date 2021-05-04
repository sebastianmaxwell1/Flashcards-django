from rest_framework import serializers
from .models import FlashcardFront


class FlashcardFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashcardFront
        fields = ['question', 'answer', 'card_number']
