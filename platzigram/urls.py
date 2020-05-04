from django.urls import path
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello, world!')

urlpatterns = [
    path('hello_world/', hello_world)
]
