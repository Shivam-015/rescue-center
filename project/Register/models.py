from django.db import models

class AnimalRescueRequest(models.Model):
    # User Information
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    # Animal Information
    ANIMAL_TYPES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Bird', 'Bird'),
        ('Other', 'Other'),
    ]
    animal_type = models.CharField(max_length=50, choices=ANIMAL_TYPES)
    animal_image = models.ImageField(upload_to='animal_rescue_images/', blank=True, null=True)

    # Location Details
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    city = models.CharField(max_length=100)

   

    def _str_(self):
        return f"{self.full_name} - {self.animal_type} ({self.city})"