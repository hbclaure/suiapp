from django.contrib import admin
from . models import CountryData,deadlifting,sideshoulder,frontshoulder,squatting,backpull,pullups


admin.site.register(CountryData)
admin.site.register(deadlifting)
admin.site.register(sideshoulder)
admin.site.register(frontshoulder)
admin.site.register(squatting)
admin.site.register(backpull)
admin.site.register(pullups)

