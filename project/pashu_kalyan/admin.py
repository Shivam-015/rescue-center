from django.contrib import admin
from .models import Rescue
# Register your models here.

@admin.register(Rescue)
class indexAdmin(admin.ModelAdmin):
    list_display = ['center_name', 'registration_number', 'email', 'phone', 'address', 'city', 'state', 
                    'pincode', 'landmark', 'facilities', 'file_12a', 'file_13a']
    
    search_fields = ['center_name', 'registration_number', 'email', 'phone', 'address', 'city', 'state', 
                     'pincode', 'landmark', 'facilities', 'file_12a', 'file_13a']
    
    list_filter = ['center_name', 'registration_number', 'email', 'phone', 'address', 'city', 'state', 
                   'pincode', 'landmark', 'facilities', 'file_12a', 'file_13a']
    list_per_page = 10