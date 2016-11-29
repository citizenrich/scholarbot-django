from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.template import loader

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import json

class Index(View):

    def get(self, request):
        return HttpResponse('yo yo')


class Alexa(View):

    def __init__(self):
        self.testing = {
              "version": "1.0",
              "sessionAttributes": {"session": "first question"},
              "response": {
                "outputSpeech": {"type": "PlainText", "text": "This is a big, fat test. Hi Rick."},
                "card": {"type": "Simple", "title": "Heyo", "content": "Hi Richard. You're a great programmer."},
                "reprompt": {"outputSpeech": {"type": "PlainText", "text": "Can I help you with anything else?"}},
                "shouldEndSession": "true"}
        }


    def post(self, request):
        body_str = request.body.decode('utf-8')
        body_json = json.loads(body_str)
        intent = body_json['request']['intent']['name']
        print(intent)
        # if intent == 'GetLatest':
        # keyword = request.POST['request']['intent']['slots']['keyword']
        return JsonResponse(self.testing)
