from django.shortcuts import render

from books.models import Book

def book_list_view(request):
    books = Book.objects.all()

    if sort := request.GET.get('sort'):
        books = books.order_by(sort)
    
    if year := request.GET.get('year'):
        books = books.filter(publish_date__year=year)

    return render(request, 'books/book_list.html', {
        'books': books,
        'sort': sort,
        'year': year,
    })
