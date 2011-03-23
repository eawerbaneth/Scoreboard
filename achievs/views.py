# Create your views here.
from achievs.models import Achievement, Level
#from achievs.models import Silver, Bronze
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

def results(request, achiev_id):
	p=get_object_or_404(Achievement, pk=achiev_id)
	return render_to_response('achievs/achievement_results.html', {'achiev': p})

# def compile(request, achiev_id):
	# p = get_object_or_404(Achievement, pk=achiev_id)
	# selected_level=p.level_set.get(pk=request.POST['level'])
	# selected_level.complete=True
	# selected_level.save()
	# return HttpResponseRedirect(reverse('achievs.views.results',args= (p.id,)))