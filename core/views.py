#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: views.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-07-08
"""

from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})
