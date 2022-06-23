from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class Movie(models.Model):
    RUB = 'RUB'
    USD = 'USD'
    EUR = 'EUR'
    NOW_YEAR = datetime.date.today().year
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollar'),
        (RUB, 'Rubles'),
    ]

    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    name = models.CharField(max_length=40)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)])  # от скольки до скольки принимать значения
    year = models.IntegerField(null=True, blank=True,  # бланк отвечает за возможность сохранить пустое поле
                               validators=[MinValueValidator(1950), MaxValueValidator(NOW_YEAR)],
                               default=2022)
    budget = models.IntegerField(validators=[MinValueValidator(1)], )
    slug = models.SlugField(default='', null=False, db_index=True)

    def __str__(self):
        return f'{self.name} - {self.rating}%'

    def get_url(self):
        return reverse('movie-detail', args=[self.slug, ])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)
