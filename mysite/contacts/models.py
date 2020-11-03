from django.db import models


class Contact(models.Model):
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, null=True, blank=True, verbose_name='Отчество')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    phone = models.CharField(max_length=250, verbose_name='Номер телефона')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='Email')
    social_page_networks = models.CharField(max_length=25, null=True, blank=True, verbose_name='Страницы в соц. сетях')
    deck = models.TextField(max_length=250, default='Подозрительная личность', verbose_name='Описание')

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
