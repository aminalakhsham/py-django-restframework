from django.db import models
from user.models import User


class Book(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    category = models.CharField(max_length=20)
    pub_date = models.DateField(verbose_name="Publish Date")
    status = models.CharField(max_length=8)
    availabe = models.BooleanField(default=True)
    book_owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class BookOffer(models.Model):
    offer_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    value = models.FloatField()

    def __str__(self):
      return "Offer Owner: " + User.objects.filter({'id': self.offer_owner})
