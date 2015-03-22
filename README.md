--This is a food truck locator app for SF, website can be visited at
http://plasma-climber-89216.appspot.com/

--Problem:
   This is a project for Uber Code Challange: https://github.com/uber/coding-challenge-tools/blob/master
	Create a service that tells the user what types of food trucks might be found near a specific location on a map.
	Data can be found: https://data.sfgov.org/Economy-and-Community/Mobile-Food-Facility-Permit/rqzj-sfat?

--Thoughts:
Before develop this web app, I have no idea of web development. 
Withinin a  week, I learned HTML, CSS, Javascript, Python, Django, MySQL, Google AppEngine.
I know this is just a prototype, and does not have many features. But it worked!
I think this is fun and enjoyable. 

--Solution:
-Structure
For the backend, the code is written in Python/Django + MySQL.
For the frontend, the code is written in Javascript, and uses Google Map API 

With Django framework, the whole web app can be decomposed into three components. 
 
1-Model: 
	FoodTruck = {id, applicant, facilityType, foodItems, latitude, longitude}
    This schema is used in MySQL database, and a corresponding Django model is created in ./hello/models.py
2-View:
	A single view called "views.py" is created in ./hello/views.py. It is registered with the homepage of the website in urls.py
	In the view.py, a SQL query is run on the MySQL database, which is hosted on Google's Cloud SQL.
	The returned SQL query result is transformed into JSON format.
	The JSON data, containing food trucks' data, is then renderred in the template file ./hello/templates/hello/home.html

3-Template:
	The html template file home.html has two major components. In the head of html, I called Google MAP API, it renders google map 
    on the home.html. Second, in the body of tempalte, I used Django's template language to receive JSON data from Views. This data 
	is used to plot truck markers on the map. So that, all the trucks' location can be shown on the map. 

-Data Flow:
	The data was first download from https://data.sfgov.org/Economy-and-Community/Mobile-Food-Facility-Permit/rqzj-sfat?
    with JSON format. Using Python, it is loaded into local MySQL database. With "mysqldump" command, the table is save in
	 ./hello_foodtruck.sql. Then, this file is uploaded to Google's Cloud Storage, and imported to the Google Could MYSQL database.

	When the http request comes in, the views.py module queries the cloud MySQL database, then transfer the data into JSON format. 
	After renderring in the html template, the data is transferred to the frontend. The Javascript, then parse the JSON data, plot 
	the trucks on the map.

--To-Do-List
A better domin name is needed
-UX:
Many features are missing. User may want to search a foodtruck, may want to search a certain type of food, may want to know the 
truck's schedule, menu, phone number and website. User may want a link to the foodtruck's website. A phone user may want to call the foodtruck inside the app. 

The markers on the map are too crowded. With a large region shown on map, there is no need to show each marker on the map, 
instead, a number can represent how many foodtrucks in that region. 

For the food-truck-owners, they may want to register their data into our system. This website should support this. 

The website should be more beautiful.

-Backend:

The models may not be complete. In the future, more information of the foodtruck maybe needed. For example, the telphone number, 
the website, the schedule of the foodtruck. 
For the purpose of foodtruck-social, our users may want to sign-up. So, more tables (models) are needed in the future. 

The foodtruck maybe moving, so the backend data needs to be refreshed reguarly. 
The foodtruck owners may want their logs shown on the map. 


Since there cannot be billions of foodtruck, the dataset is not very large. So, MySQL is good choice. 
If we are lucy, the foodlocator app gets popular, the traffic scaling can be automatically handled by Google APP Engine. 
 











