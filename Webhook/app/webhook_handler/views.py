from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import EmailEvent, Logs
import json
from django.http import HttpResponseBadRequest
from django.dispatch import receiver



def home(request):
    return render(request, "home.html")

@csrf_exempt
def sendgrid_webhookx(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        for event in data:
            email_event = EmailEvent.objects.create(
                email=event.get('email'),
                timestamp=event.get('timestamp'),
                smtp_id=event.get('smtp-id'),
                event=event.get('event'),
                ip=event.get('ip', None),
                category=event.get('category', None),
                sg_event_id=event.get('sg_event_id'),
                sg_message_id=event.get('sg_message_id'),
                response=event.get('response', None),
                attempt=event.get('attempt', None),
                sg_machine_open=event.get('sg_machine_open', None),
                useragent=event.get('useragent', None),
                url=event.get('url', None),
                bounce_classification=event.get('bounce_classification', None),
                reason=event.get('reason', None),
                status=event.get('status', None)
            )
            email_event.save()
            # Atualize o status do e-mail
            if email_event.status:
                # Tenta buscar um EmailEvent com o sg_message_id recebido
                try:
                    email_event = EmailEvent.objects.get(sg_message_id=event.get('sg_message_id'))
                    email_event.status = event.get('status', None)
                    email_event.save()
                except EmailEvent.DoesNotExist:
                    pass
            else:
                return HttpResponse(status=200)    
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=406)
    
def sendgrid_logs(request):
    logs = EmailEvent.objects.all()
    status = request.GET.get('status', None)
    if status:
        logs = logs.filter(status=status)
    logs = logs.order_by('-date_sent')
    context = {'logs': logs}
    return render(request, 'webhook_handler/sendgrid_logs.html', context)



#from snippets.models import Snippet
#from snippets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def post(self, request, format=None):
        #serializer = SnippetSerializer(data=request.data)
        
        id = request.data['sg_message_id'].split(".")
          #email = SendGridData.objects.filter(email_id=email_id).first()
        print(id[0])
        registro = Logs.objects.filter(message_id=id[0])
        if registro: 
            print("ok")
            return Response("OK", status=status.HTTP_201_CREATED)
        else:
            return Response("NOT OK", status=status.HTTP_201_CREATED)
            print(" not ok")

        return Response(request.data, status=status.HTTP_201_CREATED)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''        def get(self, request, format=None):
            snippets = Snippet.objects.all()
            serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
'''