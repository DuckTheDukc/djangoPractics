from django.contrib import admin
from library.models import Book, Publisher, Author

@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    pass
@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    pass
@admin.register(Publisher)
class AdminPublisher(admin.ModelAdmin):
    pass
# Register your models here.
