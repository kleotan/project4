from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=150)
    text = models.TextField(verbose_name="Текст", max_length=500)
    date = models.DateTimeField(auto_now=True)
    mark_like = models.BooleanField(default=False, verbose_name="Подобається")
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Автор посту")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_pk': self.pk})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'
        ordering = ['-date', 'title']
