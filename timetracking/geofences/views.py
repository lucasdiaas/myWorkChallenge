from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from geofences.models import *
import json
from django.views.decorators.csrf import csrf_exempt


#View to return a json with all the Geofences in the database
def index(request):
	data = Geofence.objects.all().values()
	data_list = list(data)
	return JsonResponse(data_list, safe=False)

#Get a string as paramenter to search a Geofence with this description
def search_geofence(request, desc):
	data = Geofence.objects.filter(desc__contains = desc).values()
	data_list = list(data)
	return JsonResponse(data_list, safe=False)

#Post method to add a Geofence to the database
@csrf_exempt
def add_geofence(request):
	print(request.method)
	if request.method == 'POST':
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		model = Geofence(**body)
		model.save()
		return HttpResponse("Success")

#Delete method, get the geofence id as paramenter in the url
@csrf_exempt
def delete_geofence(request, geofence_id):
	print(request.method)
	if request.method == 'DELETE':
		model = Geofence.objects.filter(id = geofence_id)
		model.delete()
		return HttpResponse("Success")