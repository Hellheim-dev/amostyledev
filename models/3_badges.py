db.define_table('badges',
                Field('name', type='string', readable=True, writable=False),
                Field('description', type='text', readable=True, writable=False),
                Field('icon', type='text', readable=True, writable=False),
                Field('badge_type', type='integer', readable=True, writable=False)
                )

db.define_table('badges_user',
                Field('badge_id', 'reference badges'),
                Field('user_id', 'reference auth_user'),
                Field('date_received', type='datetime')
                )