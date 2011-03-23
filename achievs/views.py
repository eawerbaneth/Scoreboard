# Create your views here.
from achievs.models import Achievement, Gold
from achievs.models import Silver, Bronze
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

#def compile(request, achiev_id)
