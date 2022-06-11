from pyexpat import model
from statistics import mode
from django.db import models

class Request(models.Model): 
    REQUEST_TYPE = (('link', 'Link'),('text', 'Text'))
    request = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=4, choices=REQUEST_TYPE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Response(models.Model):
    response = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Analysis(models.Model):
    request = models.ForeignKey("Request", on_delete=models.CASCADE)
    response = models.ForeignKey("Response", on_delete=models.CASCADE)
    turnaround_time = models.TimeField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
