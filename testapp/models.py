from __future__ import unicode_literals

from django.db import models


# Create your models here.
class deals(models.Model):
	#image=models.FileField(upload_to='uploads/')
	image=models.CharField(max_length=1000)
	deal_category=models.IntegerField()
	deal_type=models.IntegerField()
	store_name=models.CharField(max_length=100)
	store_location=models.CharField(max_length=100)
	store_address=models.TextField()
	store_phone=models.CharField(max_length=2000)
	##########to be changed to float or whatever it is
	store_latitude=models.CharField(max_length=10)
	store_longitude=models.CharField(max_length=10)
	##########
	deal_heading=models.TextField()
	deal_description=models.TextField()
	deal_validity=models.CharField(max_length=20,null=True)
	deal_activate=models.CharField(max_length=2000)
	weightage=models.IntegerField()
	deal_id=models.CharField(max_length=10)
	activate=models.IntegerField(default=0)



class contacts_db(models.Model):
	mobile=models.BigIntegerField()
	contact_details=models.TextField()

class notifications(models.Model):
	textz=models.CharField(null=True,max_length=1000)
	heading=models.CharField(max_length=1000)
	image=models.CharField(max_length=100)

class feed(models.Model):
	feeds=models.CharField(max_length=5000)
	mobile=models.BigIntegerField()