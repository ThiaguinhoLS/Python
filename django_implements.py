# -*- coding: utf-8 -*-

# urls.py -------------------------------------------------------------------------------------------------------

from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('welcome/', views.welcome, name = 'welcome'),
    path('all_book/', views.all_books, name = 'all_books'),
    re_path('detail_book/(?P<pk>', views.detail_book, name = 'detail_book'),
]

# views.py ------------------------------------------------------------------------------------------------------

from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def welcome(request):

    """ View enter in Site """
    return HttpResponse('Welcome from Site')

def all_books(request):

    """ Returns all books """
    books = Book.objects.all()
    context = {
        'books': books
        }
    return render(request, 'all_books.html', context) 

def detail_book(request, pk):

    """ Details the one book """

    try:
        book = Book.objects.get(id = pk)
    except Book.DoesNotExist:
        raise Http404
    return render(request, 'detail_book.html', context)

# forms.py ------------------------------------------------------------------------------------------------------

from django import forms

class BookForm(forms.Form):

    name = forms.CharField(max_length = 50)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 8:
            raise forms.ValidationError('Name is not valid number of characters')
        return name
    
# models.py -----------------------------------------------------------------------------------------------------

from django.db import models

class Gender(models.Model):

    name = models.Model(max_length = 30)

    def __str__(self):
        return self.name

class Book(models.Model):

    name = models.CharField(max_length = 50)
    gender = models.ForeignKey(Gender, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

# -------------------------------------------------------------------------------------------------------------

