from __future__ import unicode_literals

from django.db import models

# Create your models here.

class vouchers_db(models.Model):
	mobile=models.BigIntegerField()
	deal_id=models.CharField(max_length=10)
	voucher_id=models.CharField(max_length=10)
	activate=models.IntegerField(default=0)