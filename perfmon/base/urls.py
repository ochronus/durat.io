"""urlconf for the base application"""

from django.conf.urls import url, patterns


urlpatterns = patterns('base.views',
    url(r'^new_site/$', 'new_site', name='new_site'),
    url(r'^get_code/(.+)/$', 'get_code_for_site', name='get_code_for_site'),
    url(r'^$', 'home', name='home'),
)
