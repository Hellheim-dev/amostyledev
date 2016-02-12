# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('web',SPAN(2),'py'),XML('&trade;&nbsp;'),
                  _class="navbar-brand",_href="http://www.web2py.com/",
                  _id="web2py-logo")
response.title = 'Femmes tout terrain'
response.subtitle = ''
response.flash_level = 'info'

response.debug_message=''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Aupetit Julien'
response.meta.description = 'Ftt'
response.meta.keywords = ''
response.meta.generator = ''

## your http://google.com/analytics id
response.google_analytics_id = None



import random

from datetime import datetime

import sqlite3



QUESTION=0
ANSWER=1
COMMENT=2

MAX_POSTS=3

def get_gravatar_url(email, size=64, default='identicon'):
    import urllib, hashlib

    # construct the url
    gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'d':default, 's':str(size)})

    return gravatar_url

def set_gravatar_url(email, size=64, default='identicon'):
    import urllib, hashlib
    email = email.vars.email
    # construct the url
    gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'d':default, 's':str(size)})

    user = db(db.auth_user.email==email).select().first()
    user.update_record(gravatar_url=gravatar_url)