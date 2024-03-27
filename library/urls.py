from django.urls import path

from .views import AddBookView, ListBookView, BookDetailView 

urlpatterns = [
    path('books/',AddBookView.as_view(), name='add-book'),
    path('book/',ListBookView.as_view(),name='list-book'),
    path('books/<str:ISBN>/',BookDetailView.as_view(),name='book-detail')
]

