# utf-8
from __future__ import unicode_literals
import facebook
import urllib3
import requests
from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'Eventis/index.html')
def today(request):
  token = 'EAACEdEose0cBAFpsZAaRxweABifeAgqEl1Ax9FngbZBxZA9bZANZC4X1TCVEx5l41d1oIecZAVyQxiRBfhwE8MpnSFN11BLjMRBIkp4im1JsVDGWeZBwlWf17qZBZBLRn5v9kxQZASY9ndLKIZAfl7RHIM7pZBLohON9P8oj9bqCFtY4wdQDU6uAkXUtZBLtvYm8ZAAfYwKkXsFPKzAQZDZD'
  
  graph = facebook.GraphAPI(access_token=token, version = '2.12')
  #event = graph.get_object(id="198157354272836", fields="name, event_times")
  page = graph.get_object(id="342996209063714", fields="location")
  return render(request, 'Eventis/today.html',{
  #  'name': event['name'],
   # 'event_times': event['event_times'],
   'page_city': page['location'].get('city'),
   'page_street': page['location'].get('street'),
  })