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


def posts():

    post = {'nb_vote': 42, 'nb_answer': 5, 'nb_view': 500, 'title':'Lorem Ipsum dolor sit amet', 'date':'33/03/2012', 'author':'lambda', 'tag':['lorem', 'ipsum'], 'point': 47}

    listposts = []
    listposts.append(post)
    listposts.append(post)
    listposts.append(post)
    listposts.append(post)

    return dict(listposts=listposts)
    
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
    form2=SQLFORM(db.posts, fields=['title', 'post_content'], labels={'post_content': 'Question'}).process()

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
        log='that went wrong:<br/>'
        for error in form.errors:
            log += '&emsp;&emsp;%s: %s<br/>' %(error, form.errors[error])
        s = False
    else:
        log=''

    return dict(form=form, log=log, s=s )