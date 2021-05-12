from .models import FlashcardFront
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FlashcardFrontSerializer
from django.shortcuts import render


class FlashcardQuestions(APIView):
    # get all
    def get(self, request):
        flashcard = FlashcardFront.objects.all()
        serializer = FlashcardFrontSerializer(flashcard, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlashcardFrontSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        serializer = FlashcardFrontSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashcardDetail(APIView):
    def get_object(self, pk):
        try:
            return FlashcardFront.objects.get(pk=pk)
        except FlashcardFront.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        flashcard = self.get_object(pk)
        serializer = FlashcardFrontSerializer(flashcard)
        return Response(serializer.data)

    def put(self, request, pk):
        flashcard = self.get_object(pk)
        serializer = FlashcardFrontSerializer(flashcard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def create(request):
    #     form = FlashcardForm(request.POST or None, request.FILES or None)
    #
    #     context = {
    #         'form': form
    #     }
    #
    #     if form.is_valid():
    #         form.save()
    #         return FlashcardFront('flashcards:index')
    #
    #     else:
    #         return render(request, 'flashcards/create.html', context)

    def delete(self, request, pk):
        flashcard = self.get_object(pk)
        flashcard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
