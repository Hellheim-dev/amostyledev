# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('web',SPAN(2),'py'),XML('&trade;&nbsp;'),
                  _class="navbar-brand",_href="http://www.web2py.com/",
                  _id="web2py-logo")
response.title = request.application.replace('_',' ').title()
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