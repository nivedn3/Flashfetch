from __future__ import unicode_literals

from django.db import models

# Create your models here.
class  signup_db(models.Model):
	name=models.CharField(max_length=20)
	mobile=models.BigIntegerField(primary_key=True)
	referral=models.CharField(max_length=10)
	email=models.EmailField(null=True)
	password=models.CharField(max_length=20)
	token=models.CharField(max_length=100)
	referral_id=models.CharField(max_length=6,primary_key=True,default='test')
	otp=models.IntegerField(default=0)
	profile_id=models.CharField(max_length=6,null=True)
	no_of_refs=models.IntegerField(default=0)
	gcmid=models.CharField(max_length=1000,null=True)
	otp_ver=models.IntegerField(default=0)
	fpass=models.IntegerField(null=True)



