from django.http import HttpResponse

from datetime import datetime
import json

def hello_world(request):
    return HttpResponse('Hello, world! {now}'.format(
        now=datetime.now().strftime('%b %dth, %y - %H:%M hrs')
    ))


def hi(request):
    numbers = map(int, request.GET['numbers'].split(','))
    numbers = json.dumps(dict(enumerate(sorted(numbers))))
    # pdb.set_trace()

    return HttpResponse(
        numbers,
        content_type='application/json'
    )