from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('new/', views.add_timetrack, name='add_timetrack'),
]