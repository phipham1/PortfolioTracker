from django.db import models
from django.core.urlresolvers import reverse
import requests
import urllib
import json

from pprint import pprint

class Book(models.Model):
    def get_absoulte_url(self):
        return reverse('books:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name + '-' + self.author

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    book_image = models.CharField(max_length=1000)


#CRUD - Create, read, update, delete

#class table_name(models.Model):
 #   attributes etc.

### 11.113

#Next Step: input books app in settings.py

### 3 Steps to do to change the structure of the databases!
# 1) Go to terminal and apply: "python manage.py makemigrations books"
# 2) "python manage.py sqlmigrate books 0001"
# 3) "python manage.py migrate"

### 11.111 How to insert data in DB

# All in Terminal: python manage.py shell
# from books.models import Book
# Book.objects.all() # SEE ALL entries
# a = Book() # create a object of Book()
# add data to object a
    #a.name = "Life"
    #a.author = "ABC"
    #a.price = "10"
    #a.type "Business"
# Then save with
    #a.save()

### Check data
# a.id
# a.pk

# In [2]: Book.objects.all()
# Out[2]: <QuerySet [<Book: Life-ABC>, <Book: Success-XYZ>]>
# In [3]: Book.objects.filter(id=1)
# Out[3]: <QuerySet [<Book: Life-ABC>]>


## 11.114 - Admin panel Django
# Terminmal: "python manage.py createsuperuser"
# admin / admin123


def GetBitcoinRate():

    response = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin/')
    data = response.json()
    return data

def GetAnyCoinRate(Coinname):
    response = requests.get('https://api.coinmarketcap.com/v1/ticker/' + Coinname)
    data = response.json()
    return data






