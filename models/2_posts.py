db.define_table('post_title',
                Field('title', type='text')
                )

db.define_table('posts',
                Field('title', type='string'),
                Field('post_content', type='text'),
                Field('user_id', type='string'),
                Field('date_created', type='datetime', default=datetime.now()),
                Field('update_author', type='string'),
                Field('update_date', type='datetime', default=datetime.now()),
                Field('view_count', type='integer', default=0),
                Field('reply_count', type='integer', default=0),
                Field('vote_count', type='integer', default=0),
                Field('comment_count', type='integer', default=0),
                Field('bookmark_count', type='integer', default=0),
                Field('parent_id', type='integer', default=0),
                Field('root_id', type='integer', default=0),
                #Field('thread_score', type='integer', readable=True, writable=False),
                Field('status', type='integer', default=0),
                Field('post_type', type='integer', default=0),
                Field('has_accepted', type='boolean', default=False),
                Field('stycky', type='boolean', default=False),
                Field('changed', type='boolean', default=False)
                )

db.define_table('post_postviews',
                Field('post_id', db.posts),
                Field('ip', type='string'),
                Field('date_viewed', type='datetime')
                )

db.define_table('post_bookmarks',
                Field('post_id', db.posts),
                Field('user_id', db.auth_user),
                Field('date_bookmaked', type='datetime')
                )

db.define_table('post_vote',
                Field('post_id', db.posts),
                Field('user_id', db.auth_user),
                Field('date_voted', type='datetime')
                )

db.define_table('tags',
                Field('name', type='string'),
                Field('date_created', type='datetime')
                )

db.define_table('post_tags',
                Field('post_id', db.posts),
                Field('tag', db.tags)
                )
