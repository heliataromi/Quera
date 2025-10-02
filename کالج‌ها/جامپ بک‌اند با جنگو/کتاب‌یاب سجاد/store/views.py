from django.shortcuts import render

from .models import Book

def book_list(request):
    title = request.GET.get("title") or ''
    author = request.GET.get("author") or ''
    min_price = request.GET.get("min_price") or 0
    max_price = request.GET.get("max_price") or 150000

    books = (Book.objects.all()
             .filter(title__icontains=title, author__icontains=author, price__gte=min_price, price__lte=max_price)
             .order_by('-price'))

    context = {
        "books": books,
        "query": request.GET
    }
    return render(request, "books.html", context)
