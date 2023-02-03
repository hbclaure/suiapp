from django import forms
from .models import CountryData,deadlifting,sideshoulder,frontshoulder,squatting,backpull,pullups

class CountryDataFrom(forms.ModelForm):
	class Meta:
		model = CountryData
		fields = '__all__'

class deadliftingFrom(forms.ModelForm):
	class Meta:
		model = deadlifting
		fields = '__all__'

class sideshoulderFrom(forms.ModelForm):
	class Meta:
		model = sideshoulder
		fields = '__all__'

class frontshoulderFrom(forms.ModelForm):
	class Meta:
		model = frontshoulder
		fields = '__all__'

class squattingFrom(forms.ModelForm):
	class Meta:
		model = squatting
		fields = '__all__'


class backpullFrom(forms.ModelForm):
	class Meta:
		model = backpull
		fields = '__all__'



class pullupsFrom(forms.ModelForm):
	class Meta:
		model = pullups
		fields = '__all__'