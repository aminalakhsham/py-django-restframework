from rest_framework.viewsets import ModelViewSet
from django.http import (HttpResponse, JsonResponse)
from rest_framework.response import Response

from .models import (Book, BookOffer)
from .serializers import BookSerializer
import datetime


class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookOfferView(ModelViewSet):
    queryset = BookOffer.objects.all()
    serializer_class = BookSerializer


def book_filter_view(req, category):
      queryset = Book.objects.filter(category=category)
      serializer = BookSerializer(queryset, many=True)
      return JsonResponse(serializer.data, safe=False)


