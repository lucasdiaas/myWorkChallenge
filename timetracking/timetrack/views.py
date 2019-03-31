from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from timetrack.models import *
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#View to list all timetracks on the database
def index(request):
	data = TimeTrack.objects.all().values()
	data_list = list(data)
	return JsonResponse(data_list, safe=False)

#Post method to add a timetrack to the database
@csrf_exempt
def add_timetrack(request):
	print(request.method)
	if request.method == 'POST':
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		model = TimeTrack(**body)
		model.save()
		return HttpResponse("Success")