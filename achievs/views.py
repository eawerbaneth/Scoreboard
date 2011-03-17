# Create your views here.
from achievs.models import Achievement
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
	latest_achiev_list = Achievement.objects.all().order_by('-pub_date')[:5]
	return render_to_response('achievs/index.html', {'latest_achiev_list': latest_achiev_list})

	
def detail(request, achiev_id):
	p = get_object_or_404(Achievement,pk=achiev_id)
	return render_to_response('achievs/detail.html', {'achiev':p})
	

#examples from polls
#def results(request, poll_id):
   # return HttpResponse("You're looking at the results of poll %s." % poll_id)

#def vote(request, poll_id):
    #return HttpResponse("You're voting on poll %s." % poll_id)