from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index')
    path('', views.FlashcardQuestions.as_view()),
    # path('new/', views.create, name='create'),
    path('flashcards/<int:pk>', views.FlashcardDetail.as_view()),
    path('flashcards/<int:pk>', views.FlashcardQuestions.as_view)
]
