from django.db import models


class BuildingsBase(models.Model):
    year = models.PositiveIntegerField('Год постройки')
    area = models.CharField('Квартал', max_length=500)
    residence_name = models.CharField('Название ЖК', max_length=100)
    builder = models.CharField('Застрощик', max_length=50)

    def __str__(self):
        return self.year

    class Meta:
        verbose_name = 'Новостройка'
        verbose_name_plural = 'Новостройки'
        db_table = 'BuildingsBase'
