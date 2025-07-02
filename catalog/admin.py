from django.contrib import admin

from .models import Author, Book, BookInstance, Language, Genre

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Language)