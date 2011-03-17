from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('achievs.views',
	(r'^$', 'index'),
	(r'^(?P<achiev_id>\d+)/$', 'detail'),

    #(r'^achievs/(?P<achiev_id>\d+)/results/$', 'achievs.views.results'),
    #(r'^achievs/(?P<achiev_id>\d+)/vote/$', 'achievs.views.vote'),

    # Example:
    # (r'^scoreboard/', include('scoreboard.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
)