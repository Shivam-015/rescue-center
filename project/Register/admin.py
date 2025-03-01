from django.contrib import admin
from .models import AnimalRescueRequest

# Register your models here.
admin.site.register(AnimalRescueRequest)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['full_name','phone_number','animal_type','animal_image','address','pincode','city']
    search_fields = ['full_name','phone_number','animal_type','animal_image','address','pincode','city']
    list_filter = ['full_name','phone_number','animal_type','animal_image','address','pincode','city']
    list_per_page = 10