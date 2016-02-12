# -*- coding: utf-8 -*-

def index():

    post = db((db.posts.id>0) & (db.posts.post_type==QUESTION)).select(join=db.posts.on(db.posts.user_id==db.auth_user.id))

    posts_tags=dict()
    for p in post:
        tags=db(db.post_tags.post_id==p.posts.id).select(join=db.post_tags.on(db.post_tags.tag==db.tags.id))
        posts_tags[p.posts.id] = tags

    return dict(listposts=post, tags=posts_tags)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def post():
    log=''
    s=None
    post=db(db.posts.id==request.args[0]).select(join=db.posts.on(db.posts.user_id==db.auth_user.id))

    reply=db(db.posts.root_id==request.args[0]).select(join=db.auth_user.on(db.posts.user_id==db.auth_user.id))

    replyform = FORM(DIV(TEXTAREA(_name='answer', _class='text form-control', _type='text', requires=IS_NOT_EMPTY()), _class='col-sm-9'),
                     DIV(INPUT(_type='submit', _class='btn btn-primary'),_class='col-sm-9 col-sm-offset-3'), _class='form-horizontal')

    posts_tags=dict()
    title=''
    for p in post:
        tags=db(db.post_tags.post_id==p.posts.id).select(join=db.post_tags.on(db.post_tags.tag==db.tags.id))
        posts_tags[p.posts.id] = tags
        title=p.posts.title

    if replyform.accepts(request, session):
        db.posts.insert(title=title, post_content=replyform.vars.answer, user_id=auth.user.id, root_id=request.args[0],
                        post_type=1)
        row = db(db.posts.id == request.args[0]).select(db.posts.reply_count)
        db(db.posts.id == request.args[0]).update(reply_count=row[0].reply_count + 1)
        log=T('You answer has been submited.')
        s = True
        reply=db(db.posts.root_id==request.args[0]).select(join=db.auth_user.on(db.posts.user_id==db.auth_user.id))

    elif replyform.errors:
        log='Something went wrong:<br/>'
        for error in replyform.errors:
            log += '&emsp;&emsp;%s: %s<br/>' %(error, replyform.errors[error])
        s = False



    return dict(p=post, r=reply,  tags=posts_tags, replyform=replyform, log=log, s=s)

def faq():
    return dict()

def cgu():
    return dict()
@auth.requires_login()
def account():
    return dict()

def community():
    users = db(db.auth_user.id>0).select()


    return dict(users=users)

@auth.requires_login()
def newpost():
    log=''
    s=None

    form = FORM(DIV(LABEL(T('Title'),_class='control-label col-sm-3',),
                DIV(INPUT(_name='title', _class='form-control string', requires=IS_NOT_EMPTY()), _class='col-sm-9'),
                _class='form-group is-empty'),
                DIV(LABEL(T('Question'),_class='col-sm-9 control-label col-sm-3',),
                DIV(TEXTAREA(_name='question', _class='text form-control', _type='text', requires=IS_NOT_EMPTY()), _class='col-sm-9'),
                _class='form-group is-empty'),
                DIV(LABEL(T('tags'),_class='control-label col-sm-3',),
                DIV(INPUT(_name='tags', _class='form-control string', requires=IS_NOT_EMPTY()), _class='col-sm-9'),
                _class='form-group is-empty'),
                DIV(INPUT(_type='submit', _class='btn btn-primary'),_class='col-sm-9 col-sm-offset-3'),
                _class='form-horizontal')

    if form.accepts(request, session):
        idpost = db.posts.insert(title=form.vars.title, post_content=form.vars.question, user_id=auth.user.id)
        tagids=[]
        for tag in form.vars.tags.split(' '):
            try:
                tagids.append(db.tags.insert(name=tag))
            except sqlite3.IntegrityError:
                querry=db(db.tags.name==tag).select(db.tags.id)[0]['id']
                tagids.append(querry)
        for id in tagids:
            db.post_tags.insert(post_id=idpost, tag=id)
        log=T('You question has been asked.')
        s = True
    elif form.errors:
        log='Something went wrong:<br/>'
        for error in form.errors:
            log += '&emsp;&emsp;%s: %s<br/>' %(error, form.errors[error])
        s = False


    return dict(form=form, log=log, s=s )

@auth.requires_login()
def votes():
    votes = db(db.post_vote.user_id==auth.user_id).select(join=db.posts.on(db.posts.id==db.post_vote.post_id))

    return dict(votes=votes)


@auth.requires_login()
def bookmarks():
    books = db(db.post_bookmarks.user_id==auth.user_id).select(join=db.posts.on(db.posts.id==db.post_bookmarks.post_id),
                                                               left=db.auth_user.on(db.post_bookmarks.user_id==db.auth_user.id))


    return dict(bookmarks=books)


def ajax_vote():

    count = db((db.post_vote.post_id==request.args[0]) & (db.post_vote.user_id==auth.user.id)).count()
    if count == 0:
        db.post_vote.insert(post_id=request.args[0], user_id=auth.user.id)
        post = db(db.posts.id==request.args[0]).select().first()
        post.update_record(vote_count=post.vote_count+1)
    return post.vote_count

def ajax_bookmark():
    count = db((db.post_bookmarks.post_id==request.args[0]) & (db.post_bookmarks.user_id==auth.user.id)).count()
    if count == 0:
        db.post_bookmarks.insert(post_id=request.args[0], user_id=auth.user.id)
        post = db(db.posts.id==request.args[0]).select().first()
        post.update_record(bookmark_count=post.bookmark_count+1)
        result=T('Bookmark added.')
    else:
        db((db.post_bookmarks.post_id==request.args[0]) & (db.post_bookmarks.user_id==auth.user.id)).delete()
        post = db(db.posts.id==request.args[0]).select().first()
        post.update_record(bookmark_count=post.bookmark_count-1)
        result=T('Bookmark removed.')
    return result
