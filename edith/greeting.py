# -*- coding: utf-8 -*-
"""This module contains the dialogue states for the 'greeting' domain
in the MindMeld home assistant blueprint application
"""
from .root import app


@app.handle(intent='greet')
def greet(request, responder):
    responder.reply('Hi, I am your travel assistant.')


@app.handle(intent='exit')
def exit(request, responder):
    responder.reply('Bye!')
