from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index')
    path('', views.FlashcardQuestions.as_view()),
    path('flashcards/<int:pk>', views.FlashcardDetail.as_view()),
]
