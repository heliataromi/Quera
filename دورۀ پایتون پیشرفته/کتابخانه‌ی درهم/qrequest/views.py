from django.shortcuts import render
from qrequest.models import *
from django.http import JsonResponse

def showmathbooks(request):
    b = Book.objects.get_or_create(name='f',category="math")
    mathbooks = Book.objects.filter(category='math')
    books = []
    for book in mathbooks:
        books.append({'name': book.name, 'category': book.category})
    return JsonResponse(books, safe=False)

def showphysicsbooks(request):
    b = Book.objects.get_or_create(name='The Road to Reality', category='physic')
    b2 = Book.objects.get_or_create(name='Something Deeply Hidden', category='physic')
    physicbooks = Book.objects.filter(category='physic')
    books = []
    for book in physicbooks:
        books.append({'name': book.name, 'category': book.category})
    return JsonResponse(books, safe=False)

def showchessbooks(request):
    b = Book.objects.get_or_create(name="f",category="chess")
    chessbooks = Book.objects.filter(category='chess')
    books = []
    for book in chessbooks:
        books.append({'name': book.name, 'category': book.category})
    return JsonResponse(books, safe=False)

def showchess1books(request):
    chessbooks = Book.objects.filter(category='morf')
    books = []
    for book in chessbooks:
        books.append({'name': book.name, 'category': book.category})
    return JsonResponse(books, safe=False)