from django.urls import path
from .import views


# app_name = 'flashcards'
urlpatterns = [
    # path('', views.index, name='index')
    path('', views.FlashcardQuestions.as_view()),
    path('flashcards/<int:pk>', views.FlashcardQuestions.as_view()),
]
