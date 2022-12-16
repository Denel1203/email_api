from django.core.mail import EmailMessage
from django.shortcuts import render
from rest_framework import viewsets

from .models import Consult
from .serializers import EnvioSerializer


def send_email():
    email = EmailMessage(
        'Title',
        (EnvioSerializer.para, EnvioSerializer.titulo, EnvioSerializer.texto),
        'my-email',
        ['my-receive-email']
    )
    email.attach_file(EnvioSerializer.file)
    email.send()


class Envio_ViewSet(viewsets.ModelViewSet):
    queryset = Consult.objects.all()
    serializer_class = EnvioSerializer



