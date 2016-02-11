
db.define_table('posts',
                Field('title', type='string'),
                Field('post_content', type='text'),
                Field('user_id', 'reference auth_user'),
                Field('date_created', type='datetime', default=datetime.now()),
                Field('update_author', 'reference auth_user', default=None),
                Field('update_date', type='datetime', default=datetime.now()),
                Field('view_count', type='integer', default=0),
                Field('reply_count', type='integer', default=0),
                Field('vote_count', type='integer', default=0),
                Field('comment_count', type='integer', default=0),
                Field('bookmark_count', type='integer', default=0),
                Field('parent_id', 'reference posts'),
                Field('root_id', 'reference posts'),
                #Field('thread_score', type='integer', readable=True, writable=False),
                Field('status', type='integer', default=0),
                Field('post_type', type='integer', default=0), #0 question, 1 answer, 2 comment
                Field('has_accepted', type='boolean', default=False),
                Field('stycky', type='boolean', default=False),
                Field('changed', type='boolean', default=False)
                )

db.define_table('post_postviews',
                Field('post_id', 'reference posts'),
                Field('ip', type='string'),
                Field('date_viewed', type='datetime')
                )

db.define_table('post_bookmarks',
                Field('post_id', 'reference posts'),
                Field('user_id', 'reference auth_user'),
                Field('date_bookmaked', type='datetime')
                )

db.define_table('post_vote',
                Field('post_id', 'reference posts'),
                Field('user_id', 'reference auth_user'),
                Field('date_voted', type='datetime')
                )

db.define_table('tags',
                Field('name', type='string', unique=True),
                Field('date_created', type='datetime', default=datetime.now())
                )

db.define_table('post_tags',
                Field('post_id', 'reference posts'),
                Field('tag', 'reference tags')
                )
