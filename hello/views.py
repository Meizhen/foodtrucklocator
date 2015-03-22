from django import http
from django.template import RequestContext, loader
from hello.models import FoodTruck
import json
import os
import MySQLdb
import collections

env = os.getenv('SERVER_SOFTWARE')
if (env and env.startswith('Google App Engine/')):
  # Connecting from App Engine
  db = MySQLdb.connect(
  unix_socket='/cloudsql/plasma-climber-89216:foodtruck',
  user='root',db='FoodTruck')
else:
  # Connecting from an external network.
  # Make sure your network is whitelisted
  db = MySQLdb.connect(
  host='173.194.84.191',
  port=3306,
  user='root',db='FoodTruck')

cursor = db.cursor()
cursor.execute('SELECT * FROM hello_foodtruck')
n_rows = int(cursor.rowcount)
rows = cursor.fetchall()
l = []

for r in rows:
  d = collections.OrderedDict()
  d['id'] = r[0]
  d['applicant'] = r[1]
  d['facilityType'] = r[2]
  d['foodItems'] = r[3]
  d['address'] = r[4]
  d['latitude'] = r[5]
  d['longitude'] = r[6]
  l.append(d)

j = json.dumps(l) 
j = j.replace("'","")#get rid of single quote, which is hard to parse in JSON, need to be fixed
j = '{\"trucks\" : ' + j + '}'#surrounded with {}

def home(request):
  template = loader.get_template('hello/home.html')
  #create context and return http request
  context = RequestContext(request, {
        'trucks_json': j,})
  return http.HttpResponse(template.render(context))
#  return http.HttpResponse(j)
