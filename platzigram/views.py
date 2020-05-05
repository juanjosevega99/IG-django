from django.http import HttpResponse

from datetime import datetime

def hello_world(request):
    return HttpResponse('Hello, world! {now}'.format(
        now=datetime.now().strftime('%b %dth, %y - %H:%M hrs')
    ))


def hi(request):
    return HttpResponse('Hi!')