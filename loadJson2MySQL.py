#load data/sf.json into db
import sys
import json
from hello.models import FoodTruck

json_data = json.load(open('./data/sf.json'))
schema = json_data['meta']['view']['columns']
trucks = json_data['data']

colNumDict = {'applicant':9, 
              'facilityType':10,
			  'address':13,
              'foodItems':19,
              'latitude':22, 
              'longitude':23} 
count = 0
for truck in trucks:
  ft = FoodTruck(applicant='',facilityType='', foodItems='',address='',latitude=0,longitude=0)
  count += 1
  print '--------- count = ' + str(count)
  for key in colNumDict:
	if key == 'foodItems': continue
    value = truck[colNumDict[key]]
    if value is None:
	  continue
    else:
      setattr(ft, key, value)
      print key + ', ' + value
    ft.save()

