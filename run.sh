#! /bin/bash
#
# run.sh
# Copyright (C) 2016 dhilipsiva <dhilipsiva@gmail.com>
#
# Distributed under terms of the MIT license.
#

PORT=9999
DATABASE_URL="sqlite:///db.sqlite3" ./manage.py runserver $PORT
