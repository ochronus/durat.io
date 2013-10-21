"""urlconf for the base application"""

from django.conf.urls import url, patterns


urlpatterns = patterns('base.views',
    url(r'^new_site/$', 'new_site', name='new_site'),
    url(r'^$', 'home', name='home'),
)
