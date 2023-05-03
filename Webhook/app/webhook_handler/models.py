from django.db import models
from datetime import datetime

class EmailEvent(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField()
    smtp_id = models.CharField(max_length=100)
    event = models.CharField(max_length=50)
    ip = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    sg_event_id = models.CharField(max_length=100)
    sg_message_id = models.CharField(max_length=100)
    response = models.CharField(max_length=100, null=True, blank=True)
    attempt = models.IntegerField(null=True, blank=True)
    sg_machine_open = models.BooleanField(null=True, blank=True)
    useragent = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    bounce_classification = models.CharField(max_length=50, null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)
    
    def __str__(self):
        return self.email

    from django.db import models

class Logs(models.Model):
    nome_campanha = models.CharField(max_length=60, null=False, blank=False)
    id_campanha = models.IntegerField(null=False, blank=False)
    message_id = models.CharField(max_length=100)
    status = models.CharField(max_length=255)
    data_hora_envio = models.DateTimeField()
    data_hora_update = models.DateTimeField(auto_now=True)
    contato_id = models.IntegerField()


'''
class SendGridEvent(models.Model):
    event_type = models.CharField(max_length=255)
    event_timestamp = models.DateTimeField()
    data = models.JSONField()
'''

