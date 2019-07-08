    
from rest_framework import serializers
from .models import (Book, BookOffer)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookOffer
        fields = "__all__"