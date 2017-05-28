from django.shortcuts import render

from django.http import HttpResponse
#import books
from .models import Book
from .models import GetBitcoinRate
#from django.template import loader
from django.shortcuts import render
from django.http import Http404

#BOOK Overview SIMPLE HTLM
def index_old(request):
    #Get all book objects
    all_books = Book.objects.all()
    html = '<h1> OLD INDEX </h1> <br>'

    for book in all_books:
        url = '/books/' + str(book.id) + '/'
        html += '<a href="' + url + '">' + str(book.name) + ' </a> <br>'

    # returns simple html
    # return HttpResponse("<h>This is the books homepage</h>")

    return HttpResponse(html)

def index(request):
    #Get all book objects
    all_books = Book.objects.all()
    bitcoinRate = GetBitcoinRate()

    # 11.128 style: template = loader.get_template('books/index.html')

    #parse data as a context
    context = {
        'all_books': all_books,
        'bitcoinRate': bitcoinRate[0]['price_usd']
    }

    # render the template for us
    # 11.128 style: return HttpResponse(template.render(context, request))

    #this has http response and render function at once
    return render(request, 'books/index.html', context)


#detailed View of Books
def detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404('This book does not exist')
    # OLD Return: return HttpResponse("<h2>Details for Book ID:" + str(book_id) + "</h2>")
    return render(request, 'books/detail.html', {'book': book})

