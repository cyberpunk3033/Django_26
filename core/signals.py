from django.conf.global_settings import AUTH_USER_MODEL
from django.db.models.signals import post_save, post_delete

from django.dispatch import receiver, Signal
from django.conf import settings

# Создание суперпользователя
@receiver(post_save, sender=AUTH_USER_MODEL)
def create_superuser_signal(sender, instance, created, **kwargs):
    if instance.is_superuser:
           print(f"Суперпользователь {instance.username} был создан")

# Удаление пользователя
@receiver(post_delete, sender=AUTH_USER_MODEL)
def send_email_on_book_delete(sender, instance, **kwargs):
      print(f"Пользователь {instance.username} была удалена из базы данных")





my_signal = Signal()

@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
  print(kwargs['msg'])