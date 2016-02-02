# -*- coding: utf-8 -*-

def index():

    return dict(message=T('Welcome to web2py!'))


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

    return(listposts=listposts)
    
    