#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: seed_db.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-07-08
"""

from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            User.objects.create_user(
                'dhilipsiva', 'dhilipsiva@gmail.com', 'test1234')
        except IntegrityError:
            print("User Already exist")
