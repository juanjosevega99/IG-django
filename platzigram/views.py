from django.http import HttpResponse

from datetime import datetime
import json


def hello_world(request):
    return HttpResponse('Hello, world! {now}'.format(
        now=datetime.now().strftime('%b %dth, %y - %H:%M hrs')
    ))


def sort_integers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'status': 'Integers sorted successfully'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )


def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Platzigram'.format(name)
    return HttpResponse(message)
