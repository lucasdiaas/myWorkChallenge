from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('search/<str:desc>', views.search_geofence, name='search'),
	path('new/', views.add_geofence, name='add_geofence'),
	path('delete/<int:geofence_id>', views.delete_geofence, name='delete_geofence'),
]