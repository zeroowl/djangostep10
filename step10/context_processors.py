# -*- coding: utf-8 -*-
__author__ = 'zeroowl'

def debug_mode(request):
    from django.conf import settings
    return {"debug_mode": settings.DEBUG}