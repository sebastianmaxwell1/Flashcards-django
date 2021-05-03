from django.urls import path, include
# from django.views.generic import RedirectView
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('flashcards.urls')),
    # path('', RedirectView.as_view(url='/flashcards/'))

]
