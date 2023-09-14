from django.shortcuts import render
from .models import Category

from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Category)
def my_callback(*args,**kwargs):
    print(args, kwargs)