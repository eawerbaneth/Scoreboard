# Create your views here.
from achievs.models import Achievement, Level
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext


def results(request, achiev_id):
	p=get_object_or_404(Achievement, pk=achiev_id)
	return render_to_response('achievs/achievement_results.html', {'achiev': p})
	


def search(request):
	if 'q' in request.GET:
		message = 'You searched for: %r' % request.GET['q']
	else:
		message = 'You submitted an empty form.'
	return HttpResponse(message)