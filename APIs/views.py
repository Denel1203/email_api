from django.core.mail import EmailMessage
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Consult
from .serializers import EnvioSerializer
from rest_framework import views, status, generics
from django.core.mail import send_mail


class Sender(views.APIView):
    def get(self, request):
        print(request.data)
        email = {'to': 'joaorocha@email.com', 'title': 'Some title', 
                 'message': 'Some message'}
        serializer = EnvioSerializer(email)

        return Response(serializer.data)



class Envio_ViewSet(viewsets.ModelViewSet):
    queryset = Consult.objects.all()
    serializer_class = EnvioSerializer



    send_mail(
            serializer_class.data['title'],
            serializer_class.data['message'],
            from_email=None,
            recipient_list=[serializer_class.data['to'],],
            fail_silently=False,
        )


    #return Response(serializer_class.data, status=status.HTTP_201_CREATED)