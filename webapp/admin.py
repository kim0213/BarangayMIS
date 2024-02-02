from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Household)
admin.site.register(Resident)
admin.site.register(FinancialAssistance)
admin.site.register(Barangay)
admin.site.register(Announcement)