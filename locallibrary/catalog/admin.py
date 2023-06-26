from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance) 
admin.site.register(Language)

class BookInstanceInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    inlines = [BookInstanceInline]

admin.site.register(Author,AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status','due_back','id','borrower')
    list_filter = ('status', 'due_back')
    

    
