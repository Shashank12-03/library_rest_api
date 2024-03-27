from rest_framework import serializers
from .models import Book

class Books_Serlizers(serializers.ModelSerializer):
    
    class Meta:
        model=Book
        fields=['id', 'title', 'author', 'pub_date', 'ISBN', 'description']
    
class Books_Detail_Serlizers(serializers.ModelSerializer):
    
    class Meta:
        model=Book
        fields="__all__"
    
