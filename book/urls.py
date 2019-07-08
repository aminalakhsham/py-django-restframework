from django.urls import (path, include)
from rest_framework.routers import DefaultRouter

from .views import (BookView, BookOfferView, book_filter_view)

router = DefaultRouter()
router.register('offers', BookOfferView)
router.register('', BookView)

urlpatterns = [
    path('filter/<category>', book_filter_view),
]

urlpatterns += router.urls
