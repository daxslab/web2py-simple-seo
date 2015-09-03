__author__ = 'cccaballero'

from gluon import *
from gluon.contrib.ordereddict import OrderedDict


def set_seo_meta(type="website", card="summary", title=current.request.application.replace('_', ' ').title(),
                 author=None, keywords=None, generator="Web2py Web Framework",
                 url=URL(args=current.request.args, host=True),
                 image=None, description=None, site_name=None,
                 locale=None, locale_alternate={}, creator=None,
                 site=None, label1=None, data1=None, label2=None, data2=None):
    set_meta(title, description, keywords, author, generator)
    set_open_graph(type, title, url, image, description, site_name, locale, locale_alternate)
    set_twitter_card(card, title, creator, site, label1, data1, label2, data2, image, description)


def set_meta(title=current.request.application.replace('_', ' ').title(), description=None, keywords=None,
             author=None, generator="Web2py Web Framework"):
    current.response.title = title
    if description:
        set_description_meta(description)
    if keywords:
        set_keywords_meta(keywords)
    if author:
        set_author_meta(author)
    set_generator_meta(generator)



def set_open_graph(type="website", title=current.response.title,
                   url=URL(args=current.request.args, host=True),
                   image=None, description=current.response.meta.description,
                   site_name=None, locale=None, locale_alternate={}):
    data = locals()
    for name in ['type', 'title', 'url', 'description', 'site_name', 'locale']:
        dict = OrderedDict()
        if data[name]:
            dict['name'] = "og:"+name
            dict['content'] = data[name]
            current.response.meta['og_'+name] = dict
    if image:
        set_og_image(image)


def set_twitter_card(card="summary", title=current.response.title,
                     creator=None, site=None, label1=None,
                     data1=None, label2=None, data2=None,
                     image=None, description=current.response.meta.description):
    data = locals()
    for name in ['card', 'title', 'description', 'creator', 'site', 'label1', 'data1', 'label2', 'data2']:
        dict = OrderedDict()
        if data[name]:
            dict['property'] = "twitter:"+name
            dict['content'] = data[name]
            current.response.meta['tc_'+name] = dict
    if image:
        set_tc_image(image)


# Basic site meta


def set_description_meta(description):
    current.response.meta.description = description


def set_keywords_meta(keywords):
    current.response.meta.keywords = keywords


def set_author_meta(author):
    current.response.meta.author = author


def set_generator_meta(generator):
    current.response.meta.generator = generator

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
