import telepot
from django.db import models

from holmstroy.settings import BOT_TOKEN


# Create your models here.
class Header(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=15)
    year = models.IntegerField(null=True)
    company_description = models.TextField(null=True, max_length=150)
    user_agreement = models.FileField(upload_to='user_agreements/', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Хедер и футер'


class SlideMain(models.Model):
    title = models.CharField(max_length=300, null=True)
    page_data = models.ForeignKey(Header, on_delete=models.CASCADE, related_name='main_slide')

    class Meta:
        verbose_name_plural = 'Гланый слайд'


class IconMain(models.Model):
    header_logo = models.URLField(null=True)
    page_data = models.ForeignKey(Header, on_delete=models.CASCADE, related_name='icon_slide')

    class Meta:
        verbose_name_plural = 'Иконки'


class Product(models.Model):
    image = models.ImageField(upload_to='media/product')
    title = models.CharField(max_length=100, null=True)
    price = models.IntegerField(null=True, default='100')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Проекты'


class Services(models.Model):
    image = models.ImageField(upload_to='media/services')
    title = models.CharField(max_length=100, null=True)
    text = models.CharField(max_length=100, null=True)
    price = models.IntegerField(null=True, default='100')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Услуги'


class AboutAs(models.Model):
    image = models.ImageField(upload_to='media/about', null=True)
    text = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = 'О нас'


class Feedback(models.Model):
    image = models.ImageField(upload_to='media/services/feedback', null=True)
    text = models.CharField(max_length=500, null=True)
    FIO = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name_plural = 'Отзывы'


# Создайте экземпляр бота
bot = telepot.Bot(BOT_TOKEN)


class FeedbackPost(models.Model):
    name = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=15)  # Предполагаем, что номер телефона - строка

    def send_telegram_message(self):
        message_text = f'Пришла новая заявка!\nИмя: {self.name}\nТелефон: {self.phone_number}'
        chat_id = '680617843'
        bot.sendMessage(chat_id, message_text)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.send_telegram_message()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Заявки'


class StaticText(models.Model):
    text = models.CharField(max_length=500, null=True)
    Is_Active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Текст на сайте'


class HoweWork(models.Model):
    icon = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    text = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = 'Как мы работаем'


class Main(models.Model):
    image = models.ImageField(upload_to='media/Main')
    title = models.CharField(max_length=100, null=True)
    text = models.CharField(max_length=100, null=True)
