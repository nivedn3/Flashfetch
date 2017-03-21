from django import forms

class signup_form(forms.Form):
	mobile=forms.IntegerField()
	name=forms.CharField(max_length=20)
	email=forms.EmailField()
	password=forms.CharField(max_length=20)
	referral=forms.CharField(max_length=10,required=False)

class otp(forms.Form):
	otp_in=forms.IntegerField()
	mobile=forms.IntegerField()
	token=forms.CharField(max_length=32)

class log(forms.Form):
	mobile=forms.IntegerField()
	password=forms.CharField(max_length=20)

class rotp(forms.Form):
	mobile=forms.IntegerField()
	token=forms.CharField(max_length=32)

class fpassword(forms.Form):
	mobile=forms.IntegerField()


class pver(forms.Form):
	mobile=forms.IntegerField()
	verif=forms.IntegerField()

class cpass(forms.Form):
	mobile=forms.IntegerField()
	npass=forms.CharField(max_length=20)

class cusgcm(forms.Form):
	mobile=forms.IntegerField()
	token=forms.CharField(max_length=100)
	gcmid=forms.CharField(max_length=200)
