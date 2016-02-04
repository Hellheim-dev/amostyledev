db.define_table('post_title',
                Field('title', type='text')
                )

db.define_table('posts',
                Field('title', db.post_title, readable=True, writable=True),
                Field('post_content', type='text', readable=True, writable=True),
                Field('author', db.auth_user, readable=True, writable=False),
                Field('date_created', type='datetime', readable=True, writable=False),
                Field('update_author', db.auth_user, readable=True, writable=False),
                Field('update_date', type='datetime', readable=True, writable=False),
                Field('view_count', type='integer', readable=True, writable=False),
                Field('reply_count', type='integer', readable=True, writable=False),
                Field('vote_count', type='integer', readable=True, writable=False),
                Field('comment_count', type='integer', readable=True, writable=False),
                Field('bookmark_count', type='integer', readable=True, writable=False),
                Field('parent_id', 'reference posts', readable=False, writable=False),
                Field('root_id', 'reference posts', readable=False, writable=False),
                #Field('thread_score', type='integer', readable=True, writable=False),
                Field('status', type='integer', readable=True, writable=False),
                Field('post_type', type='integer', readable=True, writable=False),
                Field('has_accepted', type='boolean', readable=True, writable=True),
                Field('stycky', type='boolean', readable=True, writable=True),
                Field('changed', type='boolean', readable=False, writable=False)
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
