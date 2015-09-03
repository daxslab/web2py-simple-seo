__author__ = 'cccaballero'

from gluon import *
from gluon.contrib.ordereddict import OrderedDict


def set_seo_meta(type="website", card="summary", title=None,
                 author=None, keywords=None, generator="Web2py Web Framework",
                 url=None, image=None, description=None, site_name=None,
                 locale=None, locale_alternate={}, creator=None,
                 site=None, label1=None, data1=None, label2=None, data2=None):
    if not title:
        title = current.request.application.replace('_', ' ').title()
    if not url:
        url = URL(args=current.request.args, host=True)
    set_meta(title, description, keywords, author, generator)
    set_open_graph(type, title, url, image, description, site_name, locale, locale_alternate)
    set_twitter_card(card, title, creator, site, label1, data1, label2, data2, image, description)


def set_meta(title=None, description=None, keywords=None,
             author=None, generator="Web2py Web Framework"):
    data = locals()
    for name in ['title', 'description', 'keywords', 'author', 'generator']:
        if data[name]:
            current.response.meta[name] = data[name]
    if not title:
        title = current.request.application.replace('_', ' ').title()
    current.response.title = title



def set_open_graph(type="website", title=None,
                   url=None, image=None, description=None,
                   site_name=None, locale=None, locale_alternate={}):
    if not title:
        title = current.request.application.replace('_', ' ').title()
    if not url:
        url = URL(args=current.request.args, host=True)
    data = locals()
    for name in ['type', 'title', 'url', 'description', 'site_name', 'locale']:
        dict = OrderedDict()
        if data[name]:
            dict['name'] = "og:"+name
            dict['content'] = data[name]
            current.response.meta['og_'+name] = dict
    if image:
        set_og_image(image)


def set_twitter_card(card="summary", title=None,
                     creator=None, site=None, label1=None,
                     data1=None, label2=None, data2=None,
                     image=None, description=None):
    if not title:
        title = current.request.application.replace('_', ' ').title()
    data = locals()
    for name in ['card', 'title', 'description', 'creator', 'site', 'label1', 'data1', 'label2', 'data2']:
        dict = OrderedDict()
        if data[name]:
            dict['property'] = "twitter:"+name
            dict['content'] = data[name]
            current.response.meta['tc_'+name] = dict
    if image:
        set_tc_image(image)


# Open Graph meta


def set_og_image(image):
    if isinstance(image, list):
        for count in range(len(image)):
            dict = OrderedDict()
            dict['property'] = "og:image"
            dict['content'] = image[count]
            current.response.meta['og_image_'+str(count)] = dict
    else:
        dict = OrderedDict()
        dict['property'] = "og:image"
        dict['content'] = image
        current.response.meta.og_image = dict


# Twitter Card meta

def set_tc_image(image):
    dict = OrderedDict()
    dict['name'] = "twitter:image"
    if isinstance(image, list):
        dict['content'] = image[0]
    else:
        dict['content'] = image
    current.response.meta.tc_image = dict
