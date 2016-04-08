# -*- coding: utf-8 -*-
import ctypes
import os.path
import cgi
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    if request.vars.text:
        redirect(URL('meme'))
    session.counter = (session.counter or 0) + 1
    return dict(message = "", counter=session.counter)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


#@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def meme():
    import shutil
    save_path = '/memegenerator/static/'
    image_name = request.vars.upload
    #filename = request.vars.upload.filename
    #image = request.env.POST
    #shutil.copyfileobj(file, open(os.path.join(save_path, image_name), 'wb'))
    img = os.path.join(save_path, "meme.jpg") #take excisted one
    final_img = os.path.join(save_path, "meme1.jpg")
    text = request.vars.text
    lib = ctypes.CDLL('./libmeme.so')
    pfun = lib.makeMeme(img, final_img, text)
    #x = pfun("img", "final_img", "text")
    return dict(image = img)
