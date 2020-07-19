# -*- coding: utf-8 -*-
"""This module contains a template MindMeld application"""
from .root import app

from . import greeting
from . import weather

__all__ = ['app']


@app.handle(default=True)
def default(request, responder):
    """This is a default handler."""
    responder.reply('Hello there!')



def welcome(request, responder):
    prefix = 'Hello.'

    print(request)
    responder.reply( prefix + "Hi, How can I help you?")
