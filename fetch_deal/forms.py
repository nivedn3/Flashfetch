from django import forms

class  fetch(forms.Form):
	mobile=forms.IntegerField()
	token=forms.CharField(max_length=32)

class voucher_form(forms.Form):
	mobile=forms.IntegerField()
	deal_id=forms.CharField(max_length=20)
	token=forms.CharField(max_length=32)
