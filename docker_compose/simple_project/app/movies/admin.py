from django.contrib import admin
from .models import Genre, GenreFilmWork
from .models import FilmWork
from .models import Person, PersonFilmWork


class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmWork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created', 'modified')
    list_filter = ('name',)
    search_fields = ('name', 'id')


@admin.register(FilmWork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmworkInline,)
    list_display = ('title', 'type', 'creation_date',
                    'rating', 'created', 'modified')
    list_filter = ('type',)
    search_fields = ('title', 'description', 'id')


class PersonFilmworkInline(admin.TabularInline):
    model = PersonFilmWork


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = (PersonFilmworkInline,)
    list_display = ('full_name', 'created', 'modified')
    list_filter = ('full_name',)
    search_fields = ('full_name',)
