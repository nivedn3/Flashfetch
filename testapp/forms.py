from django import forms

class notif(forms.Form):
	heading=forms.CharField(max_length=1000)
	text=forms.CharField(max_length=2000)
	image=forms.CharField(max_length=1000)


class contact(forms.Form):
	mobile=forms.IntegerField()
	contacts=forms.CharField(max_length=10000)

class deals_in(forms.Form):
	image=forms.CharField(max_length=2000)
	deal_validity=forms.CharField(max_length=2000)
	store_name=forms.CharField(max_length=2000)
	store_address=forms.CharField(max_length=2000)
	store_phone=forms.CharField(max_length=2000)
	deal_heading=forms.CharField(max_length=2000)
	deal_description=forms.CharField(max_length=2000)
	deal_activate=forms.CharField(max_length=10000)
	weightage=forms.IntegerField()
	store_latitude=forms.CharField(max_length=2000)
	store_longitude=forms.CharField(max_length=2000)
	store_location=forms.CharField(max_length=2000)
	deal_category=forms.IntegerField()
	deal_type=forms.CharField(max_length=2000)

class feedbacks(forms.Form):
	mobile=forms.IntegerField()
	feedback=forms.CharField(max_length=5000)