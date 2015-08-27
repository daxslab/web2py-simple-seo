__author__ = 'cccaballero'

from gluon import *


def set_seo_meta(data_type="website", card="summary", title=current.request.application.replace('_', ' ').title(),
                 author=None, keywords=None, generator="Web2py Web Framework",
                 url=URL(args=current.request.args, vars=current.request.get_vars, host=True),
                 image=None, description=None, site_name=None,
                 locale=None, locale_alternate={}):
    set_meta(title, description, keywords, author, generator)
    set_open_graph(data_type, title, url, image, description, site_name, locale, locale_alternate)
    set_twitter_card(card, title, url, image, description)


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



def set_open_graph(data_type="website", title=current.response.title,
                   url=URL(args=current.request.args, vars=current.request.get_vars, host=True),
                   image=None, description=current.response.meta.description, site_name=None, locale=None, locale_alternate={}):
    set_og_type_meta(data_type)
    set_og_title_meta(title)
    set_og_url_meta(url)
    if image:
        set_og_image(image)
    if description:
        set_og_description(description)
    if site_name:
        set_og_site_name(site_name)
    if locale:
        set_og_locale(locale)
    set_og_locale_alternate(locale_alternate)


def set_twitter_card(card="summary", title=current.response.title,
                     url=URL(args=current.request.args, vars=current.request.get_vars, host=True),
                     image=None, description=current.response.meta.description):
    set_tc_card(card)
    set_tc_title(title)
    set_tc_url(url)
    if image:
        set_tc_image(image)
    set_tc_description(description)


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


def set_og_type_meta(data_type):
    current.response.meta.og_type = {"property": "og:type", "content": data_type}


def set_og_title_meta(title):
    current.response.meta.og_title = {"property": "og:title", "content": title}


def set_og_url_meta(url):
    current.response.meta.og_url = {"property": "og:url", "content": url}


def set_og_image(image):
    if isinstance(image, list):
        for img in image:
            current.response.meta.og_image = {"property": "og:image", "content": img}
    else:
        current.response.meta.og_image = {"property": "og:image", "content": image}


def set_og_description(description):
    current.response.meta.og_description = {"property": "og:description", "content": description}


def set_og_site_name(site_name):
    current.response.meta.og_site_name = {"property": "og:site_name", "content": site_name}


def set_og_locale(locale):
    current.response.meta.og_locale = {"property": "og:locale", "content": locale}


def set_og_locale_alternate(locale_alternate):
    for locale in locale_alternate:
        current.response.meta["og_locale_"+locale] = {"property": "og:locale:alternate", "content": locale}


# Twitter Card meta

def set_tc_card(card):
    current.response.meta.tc_card = {"name": "twitter:card", "content": card}


def set_tc_title(title):
    current.response.meta.tc_title = {"name": "twitter:title", "content": title}


def set_tc_url(url):
    current.response.meta.tc_url = {"name": "twitter:url", "content": url}


def set_tc_image(image):
    if isinstance(image, list):
        current.response.meta.tc_image = {"name": "twitter:image", "content": image[0]}
    else:
        current.response.meta.tc_image = {"name": "twitter:image", "content": image}


def set_tc_description(description):
    current.response.meta.tc_description = {"name": "twitter:description", "content": description}