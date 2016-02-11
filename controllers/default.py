# -*- coding: utf-8 -*-

def index():

    post = db(db.posts.id>0).select()

    return dict(listposts=post)


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
    post=db(db.posts.id==request.args[0]).select()
    reply=db(db.posts.root_id==request.args[0]).select()

    response.debug_message=request.args[0]

    replyform = FORM(DIV(TEXTAREA(_name='answer', _class='text form-control', _type='text', requires=IS_NOT_EMPTY()), _class='col-sm-9'),
                     DIV(INPUT(_type='submit', _class='btn btn-primary'),_class='col-sm-9 col-sm-offset-3'), _class='form-horizontal')

    if replyform.accepts(request, session):
        db.posts.insert(title='', post_content=replyform.vars.answer, user_id=auth.user.first_name, root_id=request.args[0],
                        post_type=1)
        log=T('You answer has been submit.')
        s = True
    elif replyform.errors:
        log='Something went wrong:<br/>'
        for error in replyform.errors:
            log += '&emsp;&emsp;%s: %s<br/>' %(error, replyform.errors[error])
        s = False



    return dict(p=post, r=reply, replyform=replyform, log=log, s=s)

def faq():
    return dict()

def cgu():
    return dict()

def account():
    return dict()

def community():
    users = db(db.auth_user.id>0).select()


    return dict(users=users)

def newpost():
    log=''
    s=None

    form = FORM(DIV(LABEL(T('Title'),_class='control-label col-sm-3',),
                DIV(INPUT(_name='title', _class='form-control string', requires=IS_NOT_EMPTY()), _class='col-sm-9'),
                _class='form-group is-empty'),
                DIV(LABEL(T('Question'),_class='col-sm-9 control-label col-sm-3',),
                DIV(TEXTAREA(_name='question', _class='text form-control', _type='text', requires=IS_NOT_EMPTY()), _class='col-sm-9'),
                _class='form-group is-empty'),
                DIV(INPUT(_type='submit', _class='btn btn-primary'),_class='col-sm-9 col-sm-offset-3'),
                _class='form-horizontal')

    if form.accepts(request, session):
        db.posts.insert(title=form.vars.title, post_content=form.vars.question, user_id=auth.user.first_name)
        log=T('You question has been asked.')
        s = True
    elif form.errors:
        log='Something went wrong:<br/>'
        for error in form.errors:
            log += '&emsp;&emsp;%s: %s<br/>' %(error, form.errors[error])
        s = False


    return dict(form=form, log=log, s=s )