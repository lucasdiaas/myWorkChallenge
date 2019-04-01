# myWorkChallenge
TimeTracking Challenge

It contains a Django made API 'timetracking' to manage de geofences and timetracks recorded on the database.

To run this you'll need Python 3.7.2 and Django 2.1.7 

It also contains a HTML file with a script to get the user's current postion and compare it with a geofences.json file, it calculates the users distance from the geofences, and compare if it is inside the geofence radius, if it is true the script change the button status from 'disabled' to 'enable'

Just clone this repository, and run 'python manage.py runserver' from inside the 'timetracking' folder.

In this API you have the following methods:

For the GEOFENCES

Geofences have the following structure:
```json
{
"id": <integer>,
"desc": <string>,
"latitude": <decimal>,
"longitude": <decimal>,
"radius": <decimal>
}
```

GET

localhost:8000/geofences
-To return a JSON with all the geofences in the database

localhost:8000/geofences/search/<string:description>
-To search on the database for a record with a with a description that contains the parameter passed on the URL, and return as JSON

POST

localhost:8000/geofences/new/
-To send a POST request to insert a new geofence record on the database. For this use the following format to your JSON:
```json
{
  "desc": "Description",
  "latitude": "11.223344",
  "longitude": "-22.334455",         
  "radius": "120.00"
}
```

The parameters "latitude", "longitude" and "radius" must be decimal numbers, and for radius use the distance in meters.

DELETE

localhost:8000/geofences/delete/<int:id>
-To send a DELETE request with a geofence id as parameter to search it on the database and delete its record.


For the TIMETRACKS

TimeTracks have the following structure:
```json
{
"id": <int>,
"latitude": <decimal>,
"longitude": <decimal>,
"date": <datetime>
}
```

GET

localhost:8000/timetrack/
-To list all the timetracks recorded on the database

POST

localhost:8000/timetrack/new
-To send a POST request to add a new timetrack on the database. For this method use a JSON with the following format.

```json
{
"latitude": "-23.000000",
"longitude": "-50.000000",
}
```

The timetracks cannot be deleted as requested on the Challenge description
