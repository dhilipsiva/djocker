#! /bin/bash
#
# init.sh
# Copyright (C) 2016 dhilipsiva <dhilipsiva@gmail.com>
#
# Distributed under terms of the MIT license.
#

./manage.py migrate
./manage.py seed_db
echo yes | ./manage.py collectstatic
