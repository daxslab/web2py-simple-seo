# web2py-simple-seo
Simple SEO metadata plugin for web2py including Open Graph and Twitter Cards

Installation
============

- Download The plugin installer (.w2p file) and install it via the web2py interface.


Usage
=====

```python
from plugin_simple_seo.seo import set_seo_meta

set_seo_meta(title='web2py-simple-seo', 
             author="daxSlab",
             description='Simple SEO metadata plugin for web2py including Open Graph and Twitter Cards'),
             keywords='SEO,Open Graph,Twitter Cards')

```

Advanced Usage
=====

```python
from plugin_simple_seo.seo import set_seo_meta

set_seo_meta(title='web2py-simple-seo', 
             author="daxSlab",
             description='Simple SEO metadata plugin for web2py including Open Graph and Twitter Cards'),
             keywords='SEO,Open Graph,Twitter Cards',
             data_type='website', 
             card='summary',
             generator="Web2py Web Framework",
             url='http://myurl.com',
             image=['http://myurl.com/image1.jpg', 'http://myurl.com/image2.jpg'],
             site_name='OG site name'
             locale='en_US'
             locale_alternate=['fr_FR', 'es_ES']
             )

```