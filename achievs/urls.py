from django.conf.urls.defaults import *
from achievs.models import Achievement

info_dict = {
	'queryset': Achievement.objects.all(),
}

urlpatterns = patterns('',
	(r'^$', 'django.views.generic.list_detail.object_list', info_dict),
    (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
	(r'^(?P<achiev_id>\d+)/results/$', 'achievs.views.results'),
	#(r'^(?P<achiev_id>\d+)/compile/$', 'achievs.views.compile'),
)