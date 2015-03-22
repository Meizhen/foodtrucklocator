from google.appengine.ext import ndb
from django.db import models

# Create your models here.
class FoodTruck(models.Model):
  applicant = models.CharField(max_length=256)
  facilityType = models.CharField(max_length=256)
  foodItems = models.CharField(max_length=1024)
  address = models.CharField(max_length=256)
  latitude = models.FloatField()
  longitude = models.FloatField()

  def __str__(self):
    return self.applicant+', '+str(self.latitude)+', '+str(self.longitude)
  def as_json(self):
    return dict(applicant = self.applicant,
                facilityType = self.facilityType,
                foodItems = self.foodItems,
                address = self.address,
                latitude=self.latitude,
                longitude=self.longitude)
