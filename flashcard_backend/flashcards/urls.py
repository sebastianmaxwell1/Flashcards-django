from django.urls import path
from . import views

urlpatterns = [
    # path('flashcards/', views.FlashcardQuestions.as_view()),
    path('', views.FlashcardQuestions.as_view()),
    path('collection/', views.FlashcardDetail.as_view()),
    path('flashcards/<int:pk>', views.FlashcardQuestions.as_view)
]
