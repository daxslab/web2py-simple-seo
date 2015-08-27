# web2py-simple-seo
Simple SEO metadata plugin for web2py including Open Graph and Twitter Cards

Installation
============

- Download The plugin installer (.w2p file) and install it via the web2py interface.


Usage
=====

```python
from plugin_simple_seo.seo import set_seo_meta

set_seo_meta(title=T('Agilely developed custom web, mobile and desktop applications') + ': daxSlab', author="daxSlab",
             description=T('Consulting and software development micro-firm. Hire a team of agile specialists with experience in launching MVP in 30 days'),
             keywords=T('middle-size and small business, software, development, business'))

```