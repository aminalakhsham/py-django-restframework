from django.contrib import admin

from .models import (Book, BookOffer)

admin.site.register(Book)
admin.site.register(BookOffer)