from django.shortcuts import render,redirect
from .models import CountryData,deadlifting,sideshoulder,frontshoulder,squatting,backpull,pullups
from .forms import CountryDataFrom,deadliftingFrom,sideshoulderFrom,frontshoulderFrom,squattingFrom,backpullFrom,pullupsFrom

# Create your views here.

def index(request):

	data = CountryData.objects.all()
	data2 = deadlifting.objects.all()
	data3 = sideshoulder.objects.all()
	data4 = frontshoulder.objects.all()
	data5 = squatting.objects.all()
	data6 = backpull.objects.all()
	data7 = pullups.objects.all()


	if request.method == 'POST':

		if 'submit_model1' in request.POST:
			form = CountryDataFrom(request.POST)
			if form.is_valid():
				form.save()
				return redirect('/')

		elif 'submit_model2' in request.POST:
			form2 = deadliftingFrom(request.POST)
			if form2.is_valid():
				form2.save()
				return redirect('/')

		elif 'submit_model3' in request.POST:
			form3 = sideshoulderFrom(request.POST)
			if form3.is_valid():
				form3.save()
				return redirect('/')

		elif 'submit_model4' in request.POST:
			form4 = frontshoulderFrom(request.POST)
			if form4.is_valid():
				form4.save()
				return redirect('/')

		elif 'submit_model5' in request.POST:
			form5 = squattingFrom(request.POST)
			if form5.is_valid():
				form5.save()
				return redirect('/')

		elif 'submit_model6' in request.POST:
			form6 = backpullFrom(request.POST)
			if form6.is_valid():
				form6.save()
				return redirect('/')

		elif 'submit_model7' in request.POST:
			form7 = pullupsFrom(request.POST)
			if form7.is_valid():
				form7.save()
				return redirect('/')
	
	else:
		form = CountryDataFrom()
		form2 = deadliftingFrom()
		form3 = sideshoulderFrom()
		form4 = frontshoulderFrom()
		form5 = squattingFrom()
		form6 = backpullFrom()
		form7 = pullupsFrom()








	context = {
	'data': data,
	'form': form,
	'data2': data2,
	'form2': form2,
	'data3': data3,
	'form3': form3,
	'data4': data4,
	'form4': form4,
	'data5': data5,
	'form5': form5,
	'data6': data6,
	'form6': form6,
	'data7': data7,
	'form7': form7,

	}

	
	return render(request, 'dashboard/index.html', context)