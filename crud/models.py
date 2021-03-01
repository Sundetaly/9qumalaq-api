from django.db import models
from core.models import LeaderShip, News


class Country(models.Model):
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ['name']
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class CountryLeaderShip(LeaderShip):
    class Meta:
        verbose_name = 'Руководствы'
        verbose_name_plural = 'Руководства'
    image = models.ImageField(upload_to='country_leader/')
    country = models.ForeignKey('Country', related_name='leader_ships',
                                on_delete=models.SET_NULL, null=True)


class CountryNews(News):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости стран'
    image = models.ImageField(upload_to='country_news/')
    country = models.ForeignKey('Country', related_name='news',
                                on_delete=models.SET_NULL, null=True)


class City(models.Model):
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']

    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class CityLeaderShip(LeaderShip):
    class Meta:
        verbose_name = 'Лучший игрок'
        verbose_name_plural = 'Лучшие игроки'

    image = models.ImageField(upload_to='city_leader/')
    city = models.ForeignKey('City', related_name='leader_ships',
                             on_delete=models.SET_NULL, null=True)


class CityNews(News):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости городов'
    image = models.ImageField(upload_to='city_news/')
    city = models.ForeignKey('City', related_name='news',
                             on_delete=models.SET_NULL, null=True)



