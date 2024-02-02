from django.db import models


# Create your models here.
class Household(models.Model):
    name = models.CharField(max_length=55, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Resident(models.Model):
    gender_options = (
        ("M", "Male"),
        ("F", "Female")
    )
    
    last_name = models.CharField(max_length=55, null=True)
    first_name = models.CharField(max_length=55, null=True)
    middle_name = models.CharField(max_length=55, blank=True)
    gender = models.CharField(choices=gender_options, max_length=1)
    occupation = models.CharField(max_length=55, null=True)
    address = models.CharField(max_length=255, null=True)
    contact = models.PositiveIntegerField(null=True)
    household = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.last_name
    
class FinancialAssistance(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_disbursed = models.DateTimeField(null=True)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.date_disbursed

class Barangay(models.Model):
    name = models.CharField(max_length=55, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Announcement(models.Model):
    title = models.CharField(max_length=55, null=True)
    content = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    barangay = models.ForeignKey(Barangay, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
  
    
