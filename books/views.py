

#New and lean way to style pages, generic views

from django.views import generic
from .models import Book
from django.views.generic.edit import CreateView

from .models import GetBitcoinRate, GetAnyCoinRate

from .StockModel import GetMSStock


class IndexView(generic.ListView):
    template_name = 'books/index.html'
    BTC = GetBitcoinRate()[0]['price_usd']
    ETH = GetAnyCoinRate('ethereum')[0]['price_usd']
    MicrosoftStock = GetMSStock()['l_fix']
    var2 = 200

    def get_queryset(self):
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({'BTC': self.BTC, 'ETH': self.ETH, 'var2': self.var2, 'MicrosoftStock': self.MicrosoftStock})
        return context


class BookCreate(CreateView):
    model = Book
    fields = ['name', 'author', 'price', 'type', 'book_image']


class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'