from django.urls import path

from .views import AddBookView, ListBookView, BookDetailView 

urlpatterns = [
    path('api/books/',AddBookView.as_view(), name='add-book'),
    path('api/book/',ListBookView.as_view(),name='list-book'),
    path('api/books/<str:ISBN>/',BookDetailView.as_view(),name='book-detail')
]

