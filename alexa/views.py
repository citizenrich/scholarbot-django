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


class AlexaTest(View):

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
        return JsonResponse(self.testing)

class AlexaProd(View):

    def __init__(self):

        self.empty = {
              "version": "1.0",
              "response": {
                "outputSpeech": {"type": "PlainText", "text": "Reply with a key word to search."},
                "card": {"type": "Simple", "title": "Reply with a keyword", "content": "Reply with a keyword."},
                "shouldEndSession": "false"}
        }
        self.template = {
              "version": "1.0",
              "sessionAttributes": {"session": "first question"},
              "response": {
                "outputSpeech": {"type": "PlainText", "text": ""},
                "card": {"type": "Simple", "title": "", "content": ""},
                "reprompt": {"outputSpeech": {"type": "PlainText", "text": ""}},
                "shouldEndSession": "true"}
        }

    def post(self, request):
        body_str = request.body.decode('utf-8')
        body_json = json.loads(body_str)
        intent = body_json['request']['intent']['name']
        if intent == 'LaunchRequest':
            return JsonResponse(self.empty)
        elif intent == 'GetLatest':
            keyword = body_json['request']['intent']['slots']['keyword']
            self.template['response']['outputSpeech']['text'] = 'This is a placeholder for a real interaction.'
            self.template['response']['card']['title'] = 'This is a placeholder.'
            self.template['response']['card']['content'] = 'This is a placeholder.'
            return JsonResponse(self.template)
        # elif intent == 'SessionEndedRequest'
