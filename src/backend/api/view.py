from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail


def mail(request):
    send_mail(
        'Test Subject',
        'Test message body',
        'kuznetsovakd04@yandex.ru',
        ['kuznetsovakd04@yandex.ru'],
        fail_silently=False,
    )
    return HttpResponse(f"Отправленно письмо")