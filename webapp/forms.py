from django import forms
from .models import *

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'barangay', 'image']

    # You can define custom widgets and add classes here
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'border-blue-400 border-2 p-2 w-64 placeholder-gray-400 rounded',
                'placeholder': 'Title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'border-blue-400 border-2 p-2 w-full h-32 resize-none placeholder-gray-400 rounded',
                'placeholder': 'Content'
            }),
            'barangay': forms.Select(attrs={
                'class': 'border-blue-400 border-2 p-2 w-64 max-w-md placeholder-gray-400 rounded',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'border-blue-400 p-2 rounded w-full',
            }),
        }
        
class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = '__all__'

    # You can define custom widgets and add classes here
        widgets = {
            'last_name': forms.TextInput(attrs={
                'class': 'border-blue-400 border-2 p-2 w-64 placeholder-gray-400 rounded',
                'placeholder': ''
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'border-blue-400 border-2 p-2 w-64 resize-none placeholder-gray-400 rounded',
                'placeholder': ''
            }),
            'middle_name': forms.TextInput(attrs={
                'class': 'border-blue-400 border-2 p-2 w-64 max-w-md placeholder-gray-400 rounded',
            }), 
            'gender': forms.Select(attrs={
                'class': 'border-blue-400 border-2 p-2 w-64 max-w-md placeholder-gray-400 rounded',
            }),
            'occupation': forms.TextInput(attrs={
                'class': 'border-blue-400 border-2 p-2 w-64 placeholder-gray-400 rounded',
                'placeholder': ''
            }),
            'address': forms.Textarea(attrs={
                'class': 'border-blue-400 border-2 p-2 w-64 max-w-md placeholder-gray-400 rounded',
                'placeholder': ''
            }),
            'contact': forms.NumberInput(attrs={
                'class': 'border-blue-400 border-2 p-2 w-64 max-w-md placeholder-gray-400 rounded',
            }),
            'household': forms.Textarea(attrs={
                'class': 'border-blue-400 border-2 p-2 w-64 max-w-md placeholder-gray-400 rounded',
            }),
        }
        
    
    