from django.contrib import admin

# Register your models here.
from .models import UserProfile, PersonalityTestResult, Pet, Adoption, Appointment, Blog

admin.site.register(UserProfile)
admin.site.register(PersonalityTestResult)
admin.site.register(Pet)
admin.site.register(Adoption)
admin.site.register(Appointment)
admin.site.register(Blog)
