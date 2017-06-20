
from django.contrib import admin
from .models import Person, Blog, Author, Entry


class ListPerson(admin.ModelAdmin):
    list_display = ('name', 'age', 'format_name')


admin.site.register(Person,ListPerson)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)

# Register your models here.
