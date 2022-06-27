from django.contrib import admin, messages
from .models import Movie, Director, Actor, DressingRoom
from django.db.models import QuerySet

admin.site.register(Director)  # для отображения в админке
admin.site.register(Actor)  # для отображения в админке


@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):  # для отображения таблицы в админке
    list_display = ['floor', 'numbers', 'actor']  # список отображения


# Класс для фильтров
class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 79', 'Высокий'),
            ('>= 80', 'Высочайший'),
        ]

    # что будет возвращаться при разных значениях фильтра value
    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 59':
            return queryset.filter(rating__gte=40, rating__lte=59)
        if self.value() == 'от 60 до 79':
            return queryset.filter(rating__gte=60, rating__lte=79)
        if self.value() == '>= 80':
            return queryset.filter(rating__gte=80)
        return self.value()


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):  # для отображения таблицы в админке
    list_display = ['name', 'rating', 'director', 'budget', 'rating_status']  # список отображения
    list_editable = ['rating', 'director', 'budget']  # список редактирования, любые кроме первого
    # ordering = ['-rating', 'name']  # сортировка
    list_per_page = 10  # количество отображаемых строк
    actions = ['set_dollars', 'set_euro']  # активная кнопка в "действие"
    search_fields = ['name']  # строка поиска по "name"
    list_filter = ['name', RatingFilter]  # колонка фильтрации
    # readonly_fields = ['year']  # поле нельзя редактировать
    prepopulated_fields = {'slug': ('name',)}  # slug будет вычисляться по полю name
    filter_horizontal = ['actors']

    # exclude = ['year']  # не показывать при создании и редактировании

    @admin.action(description='Установить валюту в доллар')  # сообщает о совершении действия
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)  # обновить все поля currency в значение USD

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, qs):
        count_updated = qs.update(currency=Movie.EUR)
        self.message_user(request,
                          f'Было обновлено {count_updated} записей',
                          messages.ERROR)  # добавить информационное сообщение об изменении # messages.ERROR визуальный характер

    # добавление новой динамической колонки в админ панель
    @admin.display(ordering='rating')  # сортировать поля по рейтингу
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'Плохо'
        if mov.rating < 70:
            return 'Не очень'
        if mov.rating < 80:
            return 'Норм'
        return 'Гуд'
