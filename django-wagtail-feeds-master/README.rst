Getting Started
---------------

**The latest release (0.1.0) breaks backward compatibility  with previous versions of Wagtail which were baseed Django 1.x. Use 0.0.8 for projects based on older versions of Wagtail**

To use Django Wagtail Feeds in a project::

    pip install django-wagtail-feeds


Remember to add ``wagtail_feeds`` to installed apps in settings file.

`django-wagtail-feeds` has a dependency on `wagtail settings` app. You must add ``wagtail.contrib.settings`` to your INSTALLED_APPS::

    INSTALLED_APPS += [
        'wagtail.contrib.settings',
        'wagtail_feeds',
    ]

Run migrations for Wagtail feeds::

    ./manage.py migrate wagtail_feeds

Add Feed settings in the Wagtail admin

.. figure:: http://i.imgur.com/aNp1VBg.png
   :alt: Wagtail admin

.. figure:: http://i.imgur.com/oRZRici.png
   :alt: Feed Settings

Finally reference it in the url.py ::

    from wagtail_feeds.feeds import BasicFeed, BasicJsonFeed, ExtendedFeed, ExtendedJsonFeed

    url(r'^blog/feed/basic$', BasicFeed(), name='basic_feed'),
    url(r'^blog/feed/extended$', ExtendedFeed(), name='extended_feed'),

    # JSON feed
    url(r'^blog/feed/basic.json$', BasicJsonFeed(), name='basic_json_feed'),
    url(r'^blog/feed/extended.json$', ExtendedJsonFeed(), name='extended_json_feed'),


