from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Chat(models.Model):
    type = models.CharField(max_length=1)
    members = models.ManyToManyField(User, verbose_name="Участник")

    def __str__(self):
        return self.type


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField("Сообщение")
    pub_date = models.DateTimeField('Дата сообщения', default=timezone.now)
    is_readed = models.BooleanField('Прочитано', default=False)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.message
